import json
import datetime as dt
import platform
from ..pydata_lib import test_glob  # example of relative import


def print_machine_stats():
    try:
        from ..pydata_lib import test_glob
    except RuntimeError:
        print('relative import failed')
    print(dt.datetime.now())
    print(platform.version())
    print(platform.uname())
    print(platform.machine())
    print(platform.system())
    print(platform.processor())
    print(platform.system())

