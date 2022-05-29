import os
import signal
import subprocess
import time
import sys

"""
This script runs as the parent process. It starts signal_child.py, then sends the USR1 signal.

"""

proc = subprocess.Popen(['python3', 'signal_child.py'])
print('PARENT      : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)