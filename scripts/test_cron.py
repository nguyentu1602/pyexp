import platform
import os, getpass
from datetime import datetime
now = datetime.now()
outstr = 'wake up at: ' + str(now) + "; python ver: " + str( platform.python_version() )
env_runner = os.getlogin()
effective_runner =  getpass.getuser()

outstr = f'{outstr}; envRunner is {env_runner}; effective runner is {effective_runner}'
with open('/tmp/cron_log.txt', 'w') as lgf:  # /tmp because everyone has access there
     lgf.write(outstr)
     print(outstr)

# then added to crontab -e the below lines. Remember crontab needs to source the correct envs.
# crontab also run as the user who edit the cronfile by default 
# SHELL=/bin/bash
## every minute
# * * * * * . $HOME/.profile; python3 /home/cn/tmp/crontest/test_cr.py &>> /tmp/test_cr1.log
