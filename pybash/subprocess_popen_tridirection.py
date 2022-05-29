import subprocess
print('popen_tridirection:')

# to setup the Popen instance for reading, writing and erroring at the same time, use 3 pipes:

# printing "to both stdout and stderr" to stdout (1), and immediately redirect whatever in (1) 
# to (2), which is stderr. 
# notice that because of the redirection, the echo command didn't actually print anything to (1)
proc = subprocess.Popen(
    'cat -; echo "to both stdout and stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('pass through, i.e. in stdout:', repr(stdout_value.decode('utf-8')))
print('stderr:', repr(stderr_value.decode('utf-8')))