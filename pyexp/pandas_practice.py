"""
practice advance read-write options & strategies with pandas
"""
import pandas as pd
import matplotlib.pyplot as plt


def start():
    """set options for pandas"""
    options = {
        'display': {
            'max_columns': None,
            'max_colwidth': 25,
            'expand_frame_repr': False,  # Don't wrap to multiple pages
            'max_rows': 14,
            'max_seq_items': 50,         # Max length of printed sequence
            'precision': 4,
            'show_dimensions': False
        },
        'mode': {
            'chained_assignment': None   # Controls SettingWithCopyWarning
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f'{category}.{op}', value)  # Python 3.6+

start()
# read data - trades futures
data_dir = '/home/cn/data/sample_tick/'
trades_f = data_dir + 'ES_Sample/ES_Trades.csv'

tdf = pd.read_csv(trades_f)
# checkout the trade dataset
tdf.head()
tdf.count()


quotes_f = data_dir + 'ES_Sample/ES_Quotes.csv'


qdf = pd.read_csv(quotes_f)
qdf.head()
qdf.count()

# get top of file for limited number of rows
q_head = pd.read_csv(quotes_f, nrows=100)

# read using memory map - only use for small files on a machine with massive RAM:
q_m = pd.read_csv(quotes_f, memory_map=True)  ## map the whole file into memory and read from there to be faster
q_m.head()
q_m = None
# read using chunk size as iterator
q_reader = pd.read_csv(quotes_f, chunksize=100000)

# drop columns i don't need
tdf.drop(columns=['Sales Condition', 'Exclude Record Flag'], inplace=True)

# how many days?
tdf.groupby('Date').count()

# if I want to split into days, using the chunking methods, what do I need to do?
# define a hash function taking a group as input and give out a hash as a group name
def sub_group_hash(x):
    print(x)
    return str(x)


tdf.columns
tdf.loc[0]['Date']

import datetime as dt
import os
tmp_hdf5 = "/tmp/groupby.h5"
os.remove(tmp_hdf5)
q_reader = pd.read_csv(quotes_f, chunksize=100000)  # make a reader
# create the store and append, using data_columns where I possibily could aggregate
with pd.HDFStore(tmp_hdf5) as store:
    # loop through the chunk here
    for chunk in q_reader:
        # creat4e a grouper for each chunk using the date
        chunk_grp = chunk.groupby('Date')

        # append each of the subgroubs to a separate group in the resulting hdf file
        # this will be a loop around the sub_groups
        for gr_name, grouped_df in chunk_grp:
            gr_name = dt.datetime.strptime(gr_name, '%m/%d/%Y').strftime('%Y%m%d')

            print(gr_name)
            store.append('date_%s' % gr_name, grouped_df,
                         data_columns=['Symbol', 'Time', 'Price', 'Volume', 'Market Flag'])

# now we have an hdf file with subgroup by date
with pd.HDFStore(tmp_hdf5) as store:
    # all of the groups are now the keys of the store
    for gr_name in store.keys():
        print(gr_name)
        # this is a complete group that will fit in memory
        # grouped = store.select(gr_name)

        # perform the operation on grouped and write the new output
        # grouped.groupby(......).apply(your_cool_function)



    # print("store:\n%s" % store)
    # print("\ndf:\n%s" % store['df'])
    #
    # # get the groups
    # groups = store.select_column('df','A').unique()
    # print("\ngroups:%s" % groups)
    # # iterate over the groups and apply my operations
    # l = []
    # for g in groups:
    #     grp = store.select('df',where = [ 'A=%s' % g ])
    #     # this is a regular frame, aggregate however you would like
    #     l.append(grp[['D','E','F']].sum())
    #
    # print("\nresult:\n%s" % pd.concat(l, keys = groups))

# plotting - could be quite slow - moving here
tdf[['Price']].plot(kind='line')
plt.show()

tdf[['Volume']].plot(kind='bar')
plt.show()
tdf.head()
plt.xticks(rotation=45)

fig, ax = plt.subplots()
fig.autofmt_xdate()

tdf[0::20].groupby('Date').plot(x='Time', y='Price', ax=ax, legend=False)

plt.show()