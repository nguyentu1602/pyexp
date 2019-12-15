"""
for absolute import to work well with script running in your python dir, you need:
1 - either install your package with pip/some systems
2 - using the -m flag - i.e. running python modules as script:  python -m

https://stackoverflow.com/questions/6323860/sibling-package-imports/23542795#23542795
"""
from pyexp import roman
from pydata.pydata_lib import test_glob
from pydata.submodule.submodule import print_machine_stats


##  Actual testing ground
test_glob()
print_machine_stats()
print(roman.to_roman(12))
