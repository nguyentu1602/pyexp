# All of the previous examples assume a limited amount of interaction. 
# The communicate() method reads all of the output and waits for child process to exit before returning.
# It is also possible to write to and read from the individual pipe handles used by
# the Popen instance incrementally, as the program runs. A simple echo program that
# reads from standard input and writes to standard output illustrates this technique.


## REPEATER.PY
# The below example requires the repeater.py file
# It reads from stdin and writes the values to stdout, one line at a time until there is
# no more input. It also writes a message to stderr when it starts and stops, showing the
# lifetime of the child process.

import io
import subprocess

print('one line at a time:')

proc = subprocess.Popen(
    'python3 repeater.py',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)

stdin = io.TextIOWrapper(
    proc.stdin,
    encoding='utf-8', 
    line_buffering=True, # send data on newline
)
stdout = io.TextIOWrapper(
    proc.stdout,
    encoding='utf-8'
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())
    
remainder = proc.communicate()[0].decode('utf-8')
print(remainder)


# In contrast, all output at once:
print()
print('All output at once:')
proc = subprocess.Popen(
    'python3 repeater.py',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)
stdin= io.TextIOWrapper(
    proc.stdin,
    encoding='utf-8'
)
for i in range(5):
    line = '{}\n'.format(i)
    stdin.write(line)
stdin.flush()

output = proc.communicate()[0].decode('utf-8')
print(output)
