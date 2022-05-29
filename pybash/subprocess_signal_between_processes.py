"""
The process management examples for the os module include a demonstration of signaling 
between processes using os.fork() and os.kill(). Since each Popen instance provides a pid
attribute with the process id of the child process, it is possible to do something similar 
with subprocess. The next example combines two scripts. This child process sets up a signal
handler for the USR signal.
"""

