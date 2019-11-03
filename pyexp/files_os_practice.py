data_dir = '/home/cn/data/sample_tick/'
import os
import shutil  # higher level file operations - more choices for error handling

os.path.join('usr', 'bin', 'spam')   # join path
cur_dir = os.getcwd()   # current working dir
os.chdir('/tmp'); os.getcwd() # move around
os.chdir('/home/cn/program/python/sandbox');
os.getcwd()
if not os.path.exists('/tmp/blah'):
    os.mkdir('/tmp/blah')

os.rmdir('/tmp/blah')                                   # only work if the dir is empty
shutil.rmtree('/tmp/blah', ignore_errors=True)          # works for most dir - shutils is more adaptable

## ABS and REL paths
os.path.abspath('.')
os.path.isabs('.')
os.path.relpath('/tmp/blah')

## deal with names - split names etc.
os.path.basename(os.path.join(os.getcwd(),  'test_file.py'))
os.path.dirname(os.path.join(os.getcwd(),   'test_file.py'))
os.path.split(os.path.join(os.getcwd(),     'test_file.py'))

# zip, unzip, tar, untar etc.
shutil.disk_usage('.')

# create a new file
if not os.path.exists('/tmp/to_arc'):
    os.mkdir('/tmp/to_arc')
to_arc = '/tmp/to_arc/test_arc.txt'
with open(to_arc, 'a') as fh:  # touch behavior - will throw if no immediate dir available
    os.utime(to_arc, times=None)
    fh.writelines('\n'.join(['ha', 'asdfjalsdjadf']))  # writelines does NOT add new lines. Genius!

shutil.get_archive_formats()  # all supported formats - depending on other tools in the os

# make archive needs a dir to archive so you need to move everything into that dir first
# syntax is quite tricky
shutil.make_archive('/tmp/test_arc.txt', base_dir='to_arc', root_dir='/tmp', format='gztar')  # zip or tar work too

shutil.unpack_archive(('/tmp/test_arc.txt.tar.gz'), extract_dir='/tmp/unpack/crazy')
for root, dirs, files in os.walk('/tmp/unpack/crazy'):  ## hmm - need to review os.walk()
    print(files)

# finding directory contents
base_dir = os.environ['HOME'] + '/data/sample_tick'
# first way:
kk = os.listdir(base_dir)   # list things in that directory only - level 1
for name in kk:
    name = os.path.join(base_dir, name)
    print( name, ", is dir:", os.path.isdir(name), ", is file:", os.path.isfile(name))

# second way:
for cur_dir, subdirs, filenames in os.walk(base_dir):
    """ per iteration, list all subdirs and filenames under cur_dir, then go deeper into subdirs in the
        next iterations. It basically does a tree_walk
    """
    print( 'the current dir is %s' % cur_dir)
    for subdir in subdirs:
        print('\tthe current subdir is %s' % subdir)
    for filename in filenames:
        print('\tthe current filename is %s' % filename)
    # TODO: could use regex to detect if a file is a .gz or .csv file and then do some stuff with it


