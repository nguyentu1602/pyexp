import subprocess
print('popen_combine error output to regular output:')

# to setup the Popen instance for reading, writing and erroring at the same time, use 3 pipes:
# but for stderr, instead of using PIPE, use subprocess.STDOUT
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('pass through, i.e. in stdout:', repr(stdout_value.decode('utf-8')))
print('stderr:', repr(stderr_value))  # Return None