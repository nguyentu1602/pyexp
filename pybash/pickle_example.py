import pickle
import pathlib
import bz2         # slower but save twice as much spaces, compared to gzip


from pprint import pprint


# PART 1: the basic
dogs_dict = {'Ozzy': 3, 'Filou': 8}

filename = pathlib.Path.cwd() / 'tmp' / 'dogs.pkl' # cannot use the + operator on PosixPath object

with open(filename, 'wb') as outfile:
    pickle.dump(dogs_dict, outfile)
    

with open(filename, 'rb') as infile:
    new_dict = pickle.load(infile)
    
pprint(new_dict)


# PART 2: compressing pickle files
sfile = bz2.BZ2File('tmp/smallerfile.pkl.bz', 'w')
pickle.dump(dogs_dict, sfile)

with bz2.BZ2File('tmp/smallerfile.pkl.bz', 'rb') as inBZFile:
    dict_bz = pickle.load(inBZFile)
    pprint(dict_bz)
    
    
# PART 3: pickle and multi processing:
import multiprocessing as mp
from math import cos
p = mp.Pool(4)
p.map(cos, range(10))  # cos works, but you cannot pickle lambdas and thus cannot send it to p.map()

try:
    p.map(lambda x: 2**x, range(10))
except Exception as ex:
    pprint(f"Told you we would get exception: {ex}")
    # if we do nothing here, it's a silent catch    

# dill is a package that can serialized lambdas
import dill
dill.dump(lambda x: 2**x, open('tmp/dillfile.dill', 'wb') )

# To use multiprocessing with a lambda function, or other data types unsupported by pickle, 
# you will have to use a fork of multiprocessing called pathos.multiprocessing. 
# This package uses dill for serialization instead of pickle. Creating a Pool and mapping
# a lambda function to it is done exactly the same way as you saw before.

import pathos.multiprocessing as mp
p = mp.Pool(2)
p.map(lambda x: 2**x, range(10))
