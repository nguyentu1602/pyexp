### how to use python to replace bash as a scripting tool language?
- Modules to master:
-- argparse
    https://pymotw.com/3/argparse/

-- sys
    http://pymotw.com/2/sys/interpreter.html
    http://pymotw.com/2/sys/imports.html

-- glob
-- subprocess
    https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
    https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
-- multiprocessing
    http://pymotw.com/2/multiprocessing/basics.html
    http://pymotw.com/2/multiprocessing/communication.html

-- os
-- pathlib
-- pdb
    https://doughellmann.com/posts/pymotw-pdb-interactive-debugger/




### Lessons learned:
#### Lesson 1:
So what have you learned? Instead of replacing a series of bash commands with one Python script, it often is better 
to have Python do only the heavy lifting in the middle. This allows for more modular and reusable scripts, while also 
tapping into the power of all that Python offers. Using stdin as a file object allows Python to read input, which is 
piped to it from other commands, and writing to stdout allows it to continue passing the information through the piping system. 


#### Lesson 2: subprocess
The module has 3 APIs for working with processes:
1. The run() function, and its predecessor: call(), check_call() and check_output()
2. The class Popen is a low-level API used to build the other APIs, used for more complex stuff. The ctor for Popen takes arguments to setup the new process so the parent can communicate with it via pipes.


#### Lesson 3: run a python script from another python script
https://stackoverflow.com/questions/7152340/using-a-python-subprocess-call-to-invoke-a-python-script



