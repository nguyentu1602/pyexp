import subprocess

""" suppresssing errors by passing them to DEVNULL
"""

try: 
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,       
    )
except subprocess.CalledProcessError as err:
    print('ERROR: ', err)
else:
    print('returncode:', completed.returncode)
    print(f"stdout is {completed.stdout}")
    print(f"stderr is {completed.stderr}")
    
