import glob

# basic example no recursion:
for name in sorted(glob.glob('./tmp/*')):
    print(name)
    
# to list files in a subdirectory, the subdirectory must be included in the pattern:
for name in sorted(glob.glob('/usr/*')):
    print(name)
    
# wildcards:
for name in sorted(glob.glob('/usr/local/*/*')):
    print(name)

# single characater wildcard: ?
for name in sorted(glob.glob('/usr/?i?/')):  # lib and bin are both matched
    print(name)

# character ranges:
for name in sorted(glob.glob('/usr/local/lib/py*[0-9].[0-9]/')):  # should match both python2.7 and python3.6
    print(name)    

# escaping meta-characters:
# Sometimes it is necessary to search for files with names containing the special meta-characters 
# glob uses for its patterns. The escape() function builds a suitable pattern with the special
# characters “escaped” so they are not expanded or interpreted as special by glob.

specials = '?*['

for char in specials:
    pattern = 'dir/*' + glob.escape(char) + '.txt'
    print(f'Searching for: {pattern}')
    for name in sorted(glob.glob(pattern)):
        print(name)
    print()
    
    