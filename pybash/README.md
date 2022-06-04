### how to use python to replace bash as a scripting tool language?
- Modules to master:

-- abc
    https://pymotw.com/3/abc/index.html

-- argparse
    https://pymotw.com/3/argparse/

-- glob

-- ipython

-- logging
    https://pymotw.com/3/logging/index.html

-- multiprocessing
    http://pymotw.com/2/multiprocessing/basics.html
    http://pymotw.com/2/multiprocessing/communication.html


-- os
    https://pymotw.com/3/os/index.html

-- pathlib
    https://realpython.com/python-pathlib/

-- pdb
    https://pymotw.com/3/pdb/index.html
    https://doughellmann.com/posts/pymotw-pdb-interactive-debugger/

-- pickle
    https://www.datacamp.com/tutorial/pickle-python-tutorial

-- pydoc
    https://pymotw.com/3/pydoc/index.html

-- shutil
    https://pymotw.com/3/shutil/index.html

-- subprocess
    https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
    
    https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output

-- sys
    https://pymotw.com/3/sys/index.html

-- advanced object oriented
    https://livebook.manning.com/book/the-quick-python-book-second-edition/chapter-20/1









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



### Linux Redirection notes
#### Links
https://www.gnu.org/software/bash/manual/bash.html#Redirections
https://stackoverflow.com/questions/7526971/how-to-redirect-both-stdout-and-stderr-to-a-file


#### What do 1, 2, > and & means? #in Bash shell: 
- file descriptor 1 is stdout
- file descriptor 2 is stderr
- using > to redirect ouput is the same as using '1>'
- the ampersand & alone doesn't mean anything, because it is of the '>&' operator

#### How to read the 1>&2 redirection - there are 3 parts: "1", ">" and "&2"
- "1": take the data from output stream 1 (stdout)
- ">": redirect it
- "&2" the target output stream, which is stderr
- e.g. 'echo "interesting" 1>&2' means print echo to stdout, and copy stdout to stderr

#### How to redirect both stdout and stderr to a file/to 2 files?
  Remember that the order matter, so log_file must be before 2>&1
- Redirect both to 1 file, appending:  
    command1 >> log_file 2>&1

- Redirect stdout to logfile, and stderr to errfile: 
    command2 >> log_file 2>> err_file

- To see the output while it also gets saved to a file:
    command 2>&1 | tee log_file

- To fully understand this syntac, you mus understand execution order in bash : left to right:
    command >> file.txt 2>&1

    First, '>>file.txt' means open file.txt in append mode, and redirect *stdout* there.
    Second, '2>&1' means redirect *stderr* to *where stdout is currently going*, which conveniently is the logfile

