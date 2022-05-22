import subprocess
""" To run a process and read all of its output, set the 
    stdout value to PIPE and call communicate().
    
    the PIPE is just the common one-way IPC that we've been using: |
"""
print('read: ')

# below is a subprocess that run a command: 
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout = subprocess.PIPE
)
stdout_value = proc.communicate()[0].decode('utf-8')
# repr() is a function that returns a printable representation of the given object.
print('stdout: ', repr(stdout_value)) 
