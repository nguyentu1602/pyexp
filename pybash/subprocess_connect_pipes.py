import subprocess

"""
Multiple commands can be connected into a pipeline, similar to the way the Unix shell works, 
by creating separate Popen instances and chaining their inputs and outputs together. 
The stdout attribute of one Popen instance is used as the stdin argument for the next in 
the pipeline.

"""


# The example reproduce the commandline:
# $ cat names.txt | grep "Nguyen" | cut -f 3 -d:


cat = subprocess.Popen(
    ['cat', 'names.txt'],
    stdout=subprocess.PIPE
)

grep = subprocess.Popen(
    ['grep', 'Nguyen'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE
)

cut = subprocess.Popen(
    ['cut', '-f', '3', '-d:'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE
)

end_of_pipe = cut.stdout

print('Found Nguyens:')
for line in end_of_pipe:
    print(line.decode('utf-8').strip())

