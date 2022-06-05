"""
The logging system is made up of four interacting types of objects. 
- Logger, LogRecord, Handler, Formatter

- Each module or application that wants to log uses a Logger instance to add information to the logs. 
- Invoking the logger creates a LogRecord, which is used to hold the information in memory until 
    it is processed. 
- A Logger may have a number of Handler objects configured to receive and process log records. 
- The Handler uses a Formatter to turn the log records into output messages.

To use logging for library: simply create a logger instance for each context, using an appropriate name,
then log messages using the standard levels.


"""

import logging
import pathlib

## EXAMPLE 1: logging to file:
LOG_FILENAME = '/tmp/logging_example.out'
pathlib.Path(LOG_FILENAME).touch()

# configuring the basic logger that the module uses:
logging.basicConfig( 
    filename=LOG_FILENAME, 
    level=logging.DEBUG
)

# Only works if you run from command line: python logging_examples.py
logging.debug('this message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()
    
print(f'File: \n {body}')

## EXAMPLE 2: Rotating log files:
# Running the script repeatedly causes more messages to be appended to the file. To create a new
# file each time the program runs, pass a filemode argument to basicConfig() with a value of 'w'.
# Rather than managing the creation of files this way, though, it is better to use a RotatingFileHandler,
# which creates new files automatically and preserves the old log file at the same time.

import glob
import logging.handlers

LOG_FILENAME = '/tmp/logging_rotatingfile_example.out'
# setup a specific logger  with our desired ouput level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)


# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,  # Set maxBytes to a more appropriate value in a real program.
    backupCount=5
)

my_logger.addHandler(handler)
# log some messages:

for i in range(20):
    my_logger.debug(f'i = {i:d}')
    
# see what files are created:
logfiles = glob.glob(f'{LOG_FILENAME}*')
for filename in sorted(logfiles):
    print(filename)
    

## EXAMPLE 3: Verbosity levels:

# Logging       Levels
# CRITICAL	    50
# ERROR	        40
# WARNING	    30
# INFO	        20
# DEBUG	        10
# UNSET	        0

import sys
from importlib import reload
logging.shutdown()  # step 1 of resetting the root logger
reload(logging)     # step 2 of resetting the root logger

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level_name = level_name.lower()
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)
    
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')
    
    
## EXAMPLE 4: named logger
logging.basicConfig(level=logging.WARNING)
logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module.')
logger2.warning('This message comes from another module.')


##########################
##  THE LOGGING TREE:
########################## 
# - The Logger instances are configured in a tree structure, based on their names.
# - Typically each application/library defines a base name, with loggers for individual modules set as children.
# - The root logger has no name.

# - If a logger does not have any handlers, the message is handed to its parent for processing. 
# - This means that for most applications it is only necessary to configure handlers on the root logger,
#   and all log information will be collected and sent to the same place.
# - See https://pymotw.com/3/logging/index.html for several diagrams
# - See https://pypi.org/project/logging_tree/ if you need to print the logging tree


## EXAMPLE 5: integration with the warnings module:
# The logging module integrates with warnings through captureWarnings(), which configures warnings 
# to send messages through the logging system instead of outputting them directly.

import warnings
logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')

