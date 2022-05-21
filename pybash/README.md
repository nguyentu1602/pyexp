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

        

