'''How to code decision tree from scratch?
The original decision tree is proposed by JR Quinlan.
Quinlan's implementation search for the best feature to split at each stage, therefore
expensive.

Adele Cutler proposes a random tree approach:
http://www.interfacesymposia.org/I01/I2001Proceedings/ACutler/ACutler.pdf

Adele's main idea:
The feature i to split on at each level is determined randomly.
It is not determined using information gain or correlation, etc.
The split value for each node is determined by:
Randomly selecting two samples of data and taking the mean of their Xi values.

'''


data = [['slashdot', 'USA', 'yes', 18, 'None'], ['google', 'France', 'yes', 23, 'Premium'],
        ['digg', 'USA', 'yes', 24, 'Basic'], ['kiwitobes', 'France', 'yes', 23, 'Basic'],
        ['google', 'UK', 'no', 21, 'Premium'], ['(direct)', 'New Zealand', 'no', 12, 'None'],
        ['(direct)', 'UK', 'no', 21, 'Basic'], ['google', 'USA', 'no', 24, 'Premium'],
        ['slashdot', 'France', 'yes', 19, 'None'], ['digg', 'USA', 'no', 18, 'None'],
        ['google', 'UK', 'no', 18, 'None'], ['kiwitobes', 'UK', 'no', 19, 'None'],
        ['digg', 'New Zealand', 'yes', 12, 'Basic'], ['slashdot', 'UK', 'no', 21, 'None'],
        ['google', 'UK', 'yes', 18, 'Basic'], ['kiwitobes', 'France', 'yes', 19, 'Basic']]


class Dnode:
    def __init__(self, col=-1, val=None, results=None,
                 tb=None, fb=None):
        self.col = col # column index of the criteria to be tested
        self.val = val # val: value that the column must match to get true result
        self.results = results # dict() of results for this branch. None for everything exept endpoints
        self.tb = tb   # next node in the tree if result = true
        self.fb = fb   # next node in the tree if result = false


def divideset(rows, column, value):
    '''divide a set on a specific column'''
    split_func = None
    if isinstance(value, int) or isinstance(value, float):
        split_func = lambda row: row[column] >= value
    else:
        split_func = lambda row: row[column] == value
    #divide the rows into 2 sets and return them
    set1 = [row for row in rows if split_func(row)]
    set2 = [row for row in rows if not split_func(row)]
    return (set1, set2)


# make an uniquecounts function:
def uniquecounts(rows):
    results = {}
    for row in rows:
    # the result is the last column
        r = row[len(row) - 1]
        if r not in results:
            results[r] = 0
        results[r] += 1
    return results


"""entropy is sum(-p*log(p)) over probabilities of all groups
"""
def entropy(rows):
    from math import log
    log2 = lambda x:log(x)/log(2)
    results = uniquecounts(rows)
    # now calculate the entropy
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent = ent - p*log2(p)
    return ent


def buildtree(rows, scoref=entropy):
    if len(rows) == 0:
        return Dnode()
    current_score = scoref(rows)
    # set up some variables to track the best criteria
    best_gain = 0.0
    best_criteria = None
    best_sets = None
    column_count = len(rows[0]) - 1
    for col in range(0, column_count):
        # generage list of different vals in this col
        column_values = dict()
        for row in rows:
            column_values[row[col]] = 1
        # now try dividing the rows up for each val
        for val in column_values.keys():
            (set1, set2) = divideset(rows, col, val)
            # information gain
            p = float(len(set1)/len(rows))
            gain = current_score - p*scoref(set1) - (1-p)*scoref(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, val)
                best_sets = (set1, set2)
                # create the subbranches
        if best_gain > 0:
            trueBranch = buildtree(best_sets[0])
            falseBranch = buildtree(best_sets[1])
            return Dnode(col=best_criteria[0], val=best_criteria[1],
                         tb=trueBranch, fb=falseBranch)
        else:
            print(uniquecounts(rows))
            return Dnode(results=uniquecounts(rows))


def classify(observation, tree):
    if tree.results != None:
        return tree.results
    else:
        v = observation[tree.col]
        branch = None
        if isinstance(v, int) or isinstance(v, float):
            if v >= tree.val:
                branch = tree.tb
            else:
                branch = tree.fb
        else:
            if v == tree.val:
                branch = tree.tb
            else:
                branch = tree.fb
        return classify(observation, branch)

tree = buildtree(data)
classify(['google', 'UK', 'yes', 18], tree)
classify(['kiwitobes', 'France', 'yes', 19], tree)
