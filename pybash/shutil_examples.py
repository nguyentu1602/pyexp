import glob
import shutil
import pathlib
import os
import time

## EXAMPLE 1: copying files with copyfile()
print(f'cwd: {pathlib.Path.cwd()}')
print(f"BEFORE: {glob.glob('./pybash/shutil_examples.*')}")

shutil.copyfile('./pybash/shutil_examples.py', './pybash/shutil_examples.py.bak')

print(f"AFTER COPY: {glob.glob('./pybash/shutil_examples.*')}")

# delete file:
pathlib.Path('./pybash/shutil_examples.py.bak').unlink()     # shutil.rmtree() only works for dir

print(f"AFTER unlink(): {glob.glob('./pybash/shutil_examples.*')}")


## EXAMPLE 2: copying file with copy()
# The permissions of the file are copied along with the contents.
os.mkdir('./tmp/shutil_ex/')
print(f"Before: {glob.glob('./tmp/shutil_ex/*')}")
for txtFile in sorted(glob.glob('./tmp/*.txt')):
    shutil.copy(txtFile, './tmp/shutil_ex/' )

print(f"After: {glob.glob('./tmp/shutil_ex/*')}")


## EXAMPLE 3: copy2():
# works like copy(), but includes the access and modification times in the metadata copied to the new file.

def show_file_info(filename):
    stat_info = os.stat(filename)
    print('  Mode    :', oct(stat_info.st_mode))
    print('  Created :', time.ctime(stat_info.st_ctime))
    print('  Accessed:', time.ctime(stat_info.st_atime))
    print('  Modified:', time.ctime(stat_info.st_mtime))

for sfile in glob.glob('./tmp/*.txt'):
    print('SOURCE: ')
    show_file_info(sfile)    
    shutil.copy2(sfile, './tmp/shutil_ex/')
    print('DESTINATION: ')
    show_file_info( pathlib.Path('./tmp/shutil_ex') / pathlib.Path(sfile).name)    

## EXAMPLE 4: copymode() i.e. copying file Metadata
# copymode() to duplicate the permissions of the script to the example file.
# copystat() to duplicate other metadata
with open('./tmp/file_to_change.txt', 'wt') as f:
    f.write('content')

os.chmod('./tmp/file_to_change.txt', 0o444)
print(f"Before: {oct(os.stat('./tmp/file_to_change.txt').st_mode)}")

shutil.copymode('./pybash/shutil_examples.py', './tmp/file_to_change.txt')
print(f"After: {oct(os.stat('./tmp/file_to_change.txt').st_mode)}")


shutil.copystat('./pybash/shutil_examples.py', './tmp/file_to_change.txt')
show_file_info('./tmp/file_to_change.txt')


## EXAMPLE 5: working with directory trees - copytree() and removetree()
# shutil includes three functions for working with directory trees. To copy a directory from one place to another, use copytree(). It recurses through the source directory tree, copying files to the destination. The destination directory must not exist in advance.

import pprint
print('BEFORE: ')
pprint.pprint(glob.glob('./tmp/shutil_ex_copytree/*'))

shutil.copytree('./pyexp', './tmp/shutil_ex_copytree')

print('After copytree: ')
pprint.pprint(glob.glob('./tmp/shutil_ex_copytree/*'))


shutil.rmtree('./tmp/shutil_ex_copytree')
print('After rmtree: ')

pprint.pprint(glob.glob('./tmp/shutil_ex_copytree/*'))


## copytree() accepts two callable arguments to control its behavior. The ignore argument is called
# with the name of each directory or subdirectory being copied along with a list of the contents of
# the directory. It should return a list of items that should be copied. 
# The copy_function argument is called to actually copy the file.

def verbose_copy(src, dst):
    print(f'copying\n {src}\n to {dst}')
    return shutil.copy2(src, dst)

print('BEFORE:')
pprint.pprint(glob.glob('/tmp/shutil_example_copytree/*'))
print()

shutil.copytree(
    './pyexp', '/tmp/shutil_example_copytree',
    copy_function=verbose_copy,
    ignore=shutil.ignore_patterns('*.py'),
)

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/shutil_example_copytree/*'))


## EXAMPLE 6: move()
with open('/tmp/example.txt', 'wt') as f:
    f.write('contents')

print('BEFORE: ', glob.glob('/tmp/example*'))

shutil.move('/tmp/example.txt', '/tmp/example.out')

print('AFTER : ', glob.glob('/tmp/example*'))


## EXAMPLE 7: finding files:
print(shutil.which('python'))
print(shutil.which('ls'))
print(shutil.which('no-such-program'))  # return none


# which() takes arguments to filter based on the permissions the file has, and the search path
# to examine. The path argument defaults to os.environ('PATH'), but can be any string containing
# directory names separated by os.pathsep. The mode argument should be a bitmask matching the
# permissions of the file. By default the mask looks for executable files, but the following 
# example uses a readable bitmask and an alternate search path to find a configuration file.


