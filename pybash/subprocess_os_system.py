import subprocess

completed = subprocess.run(['ls', '-l'])  # this will run subprocess and output to stdout
print(f"return code: {completed.returncode}")

# setting the 'shell' argument to true causes subprocess to spawn an intermediate shell
# process which then runs the command. The default is to run the command directly.

# Using an intermediate shell means that variables, glob patterns, and other special shell features in the command
# string are processed before the comand is run

# WARNING: USING SHELL=TRUE IS SERIOUS SECUIRTY RISK:
# https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess

shellProcess = subprocess.run("echo $HOME", shell=True)
print(f"return code: {shellProcess.returncode}")

# The returncode attr of the CompletedProcess is the exit code of the program.
# Passing check=True to run() makes it equivalent to using check_call()


try: 
    subprocess.run(['false'], check=True) # The false comand always exist with a non-zero code status -> interp as error
except subprocess.CalledProcessError as err:
    print("Error:", err)
    
# Capturing output:
completed = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
    shell=True,   # if I don't used shell=True, then I inherit the 'ls' command from my own bash_alias
)
# NOTE: Passing check=True and setting stdout to PIPE is equivalent to using check_output().

print(f"returncode:{completed.returncode}")
print(f"Have {len(completed.stdout)} bytes in stdout:\n{completed.stdout.decode('utf-8')}")



# Series of comand in a sub-shell, sending msgs to stdout and stderr before exiting with an error code
try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print(f"ERROR: {err}")
else:
    print(f"{completed.returncode}")
    print(f"Example stderr: Have {len(completed.stdout) } in stdout: {completed.stdout.decode('utf-8')}")
    # the msg to std error is printed to the console, but the msg to stdout is hidden
    
