
## Links
https://www.gnu.org/software/bash/manual/bash.html#Redirections
https://stackoverflow.com/questions/7526971/how-to-redirect-both-stdout-and-stderr-to-a-file


## What do 1, 2, > and & means? #in Bash shell: 
- file descriptor 1 is stdout
- file descriptor 2 is stderr
- using > to redirect ouput is the same as using '1>'
- the ampersand & alone doesn't mean anything, because it is of the '>&' operator

## How to read the 1>&2 redirection - there are 3 parts: "1", ">" and "&2"
- "1": take the data from output stream 1 (stdout)
- ">": redirect it
- "&2" the target output stream, which is stderr
- e.g. 'echo "interesting" 1>&2' means print echo to stdout, and copy stdout to stderr

## How to redirect both stdout and stderr to a file/to 2 files?
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


