import pathlib
import os
import itertools
"""
- “pure” classes operates on strings but do not interact with an actual filesystem
- PurePosixPath and PureWindowsPath are pure classes
- “concrete” classes extends the API to include operations that reflect 
  or modify data on the local filesystem. Path() is concrete 
  
"""

## EXAMPLE 1: pure path classes:
usr = pathlib.PurePosixPath('/usr')
print(usr)

# operator / is overloaded. Can be run on another Path or just string
usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

# relative path works, and does not get immediately resolved, but attached another path, 
# and it will be resolved
root = usr / '..'    
print(root)

etc = root / '/etc/'
print(etc)

## EXAMPLE 2: resovle
# resolve() normalize a path by looking at the filesystem for dirs and symlinks, then
# producing the absolute path referred to by a name
usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())


## EXAMPLE 3: join path:
# to join paths when the segments are not known in advance
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)


## EXAMPLE 4: create new path from old path by replacing names:
# .with_name() or .with_suffix() both return new objects and the original left unchanged.
ind = pathlib.PurePosixPath('source/pathlib/index.rst')
print(ind)
py = ind.with_name('pathlib_from_existing.py')
print(py)

pyc = py.with_suffix('.pyc')
print(pyc)


## EXAMPLE 5: parsing paths:
# Extracting partial values from names:
p = pathlib.PurePosixPath('/usr/local')
print(p.parts)   # .parts is a property that returns a tuple of 'parts' after removing the separator value

# Moving up parents:
p = pathlib.PurePosixPath('/usr/local/lib')
print('parent: {}'.format(p.parent))
print('\nhierarchy:')
for up in p.parents:
    print(up)
    
# accessing other parts:
p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('path   : {}'.format(p))            # source/pathlib/pathlib_name.py
print('name   : {}'.format(p.name))       # pathlib_name.py 
print('suffix : {}'.format(p.suffix))     # .py
print('stem   : {}'.format(p.stem))       # pathlib_name


## EXAMPLE 6: creating concrete paths: Path.home() and Path.cwd()
home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
print( f'home: {home}')
print( f'cwd: {cwd}')


## EXAMPLE 7: directory contents:
# 3 methods for accessing the directory listings to discover the names of files available on the file system
# iterdir() is a generator, yielding a new Path instance for each item in the containing dir.
p = pathlib.Path('.')
for f in p.iterdir():     # if the Path does not refer to a directory, .iterdir() raises NotADirectoryError
    if isinstance(f, pathlib.Path) and f.is_dir():
        for ff in f.iterdir():
            print(ff)


## EXAMPLE 8: use glob() inside the pathlib library
p = pathlib.Path('./pybash')
print(p.resolve())
for f in p.glob('p*.py'):
    print(f)

# the glob processor supports recursive scanning using rglob, or the pattern previx **
for f in pathlib.Path('.').rglob('p*.py'):
    print(f)


## EXAMPLE 9: reading and writing files:
# - to immediately retrieving contents, use read_bytes() or read_text()
# - to write to the file, use write_bytes() or write_text()
# - use open() to open and retain the file handle, instead of the built-in open() function:
f = pathlib.Path('./tmp/pathlib_write_example.txt')
f.write_bytes('This is the content'.encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    print(f'read from open(): {handle.read()}')

print(f"read_text(): { f.read_text('utf-8')}" ) 
    

## EXAMPLE 10: manipulating directories and symbolic links
p = pathlib.Path('./tmp/example_dir') 
print(f'p.mkdir() to create {p}. Raise FileExistsError if exists')
# if p.exists():
#     p.unlink()
# p.mkdir()         # If the path already exists, mkdir() raises a FileExistsError.


p = pathlib.Path('./tmp/example_link') 
p.symlink_to('../pybash/names.txt')   # If the symlink already exists, raises a FileExistsError

print(p)
print(p.resolve())


## EXAMPLE 11: file types 
root = pathlib.Path('./tmp/pathlib_test_files')

# cleanup from previous runs:
if root.exists():
    for f in root.iterdir():
        f.unlink()
else:
    root.mkdir()

# create test files:
(root / 'file').write_text(
    'This is a regular file', encoding='utf-8'
)

(root / 'symlink').symlink_to('file')
os.mkfifo(str(root / 'fifo'))

# check the file types and print:
to_scan = itertools.chain(
    root.iterdir(),
    [pathlib.Path('/dev/disk0'), pathlib.Path('/dev/console')]
)

hfmt = '{:28s}' + (' {:>5}' * 6)
fmt = '{:30s}  ' + ('{!r:>5}  ' * 6)

print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block', 'Character'))
print()
for f in to_scan:
    print(fmt.format(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))


## EXAMPLE 12: file properties: stat() or lstat()
import time

p = pathlib.Path('./pybash/README.md')
stat_info = p.stat()

print(f'{p.as_posix()}:')
print(f'{p} is owned by {p.owner()}/{p.group()}')  # alphabetical name/group
print(f'    Size:{stat_info.st_size}')
print(f"    Perm:{oct(stat_info.st_size)}")
print(f'    Owner:{stat_info.st_uid}')             # numerical id
print(f'    Device:{stat_info.st_dev}')
print(f'    Created:{time.ctime(stat_info.st_ctime)}')
print(f'    Last Modified:{time.ctime(stat_info.st_mtime)}')
print(f'    Last accessed:{time.ctime(stat_info.st_atime)}')


## EXAMPLE 13: touch()
p = pathlib.Path('./tmp/touched')
if p.exists():
    print('already exists')
else:
    print('creating new')
p.touch()
start = p.stat()
time.sleep(1)

p.touch()
end = p.stat()
print('Start:', time.ctime(start.st_mtime))
print('End  :', time.ctime(end.st_mtime))


## EXAMPLE 14: permissions:
import os
import stat
# create a fresh test file.
f = pathlib.Path('./tmp/pathlib_chmod_example.txt')
if f.exists():
    f.unlink()
f.write_text('contents')

# determine what permissions are already set using stat
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print(f'Before: {existing_permissions}')

# decide which way to toggle them:
if not (existing_permissions & os.X_OK):
    print('Adding execute permission')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # use XOR to remove the user execute permission
    new_permissions = existing_permissions ^ stat.S_IXUSR

# make the change and show the new value:
f.chmod(new_permissions)

after_permissions = stat.S_IMODE(f.stat().st_mode)
print(f'After: {after_permissions}')

## EXAMPLE 15: deleting:
# different methods for dirs vs. files:

p = pathlib.Path('./tmp/example_dir')
p.rmdir()   # a FileNotFoundError exception is raised if the post-conditions are alreadyy met
# also error out id the directory is not empty

p = pathlib.Path('./tmp/touched')
p.touch()
print(f'exists before removing: {p.exists()}')
p.unlink()
print(f'exists after removing: {p.exists()}')

