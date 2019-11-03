"""
How to groupby over large file in python?
https://stackoverflow.com/questions/15798209/pandas-group-by-query-on-large-data-in-hdfstore
https://stackoverflow.com/questions/25459982/trouble-with-grouby-on-millions-of-keys-on-a-chunked-file-in-python-pandas
# need to install pytables
"""

import numpy as np
import pandas as pd
import os

fname = 'groupby.h5'

# create a frame
df = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'foo',
                         'bar', 'bar', 'bar', 'bar',
                         'foo', 'foo', 'foo'],
                   'B': ['one', 'one', 'one', 'two',
                         'one', 'one', 'one', 'two',
                         'two', 'two', 'one'],
                   'C': ['dull', 'dull', 'shiny', 'dull',
                         'dull', 'shiny', 'shiny', 'dull',
                         'shiny', 'shiny', 'shiny'],
                   'D': np.random.randn(11),
                   'E': np.random.randn(11),
                   'F': np.random.randn(11)})

# create the store and append, using data_columns where I possibily could aggregate
with pd.HDFStore(fname) as store:
    store.append('df', df, data_columns=['A', 'B', 'C'])
    print("store:\n%s" % store)
    print("\ndf:\n%s" % store['df'])

    # get the groups
    groups = store.select_column('df','A').unique()
    print("\ngroups:%s" % groups)
    # iterate over the groups and apply my operations
    l = []
    for g in groups:
        grp = store.select('df',where = [ 'A=%s' % g ])
        # this is a regular frame, aggregate however you would like
        l.append(grp[['D','E','F']].sum())

    print("\nresult:\n%s" % pd.concat(l, keys = groups))

os.remove(fname)