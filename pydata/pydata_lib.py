import os
import glob
import pprint


def test_glob():
    """test the glob package"""
    pp = pprint.PrettyPrinter()
    pp.pprint('Testing glob features')
    pp.pprint(glob.glob('./**/*.py'))  # nested and list all .py files


