import os
from datetime import datetime

# Get path
print(os.getcwd())

# Change path
os.chdir('/Users/hugotorche/Data/')
print(os.getcwd())

# Print all path directories
print(os.listdir())

# Add directories
os.makedirs('OS-Demo-1/Sub-Dir-1')
print(os.listdir())

# Remove directories
os.removedirs('OS-Demo-1/Sub-Dir-1')
print(os.listdir())

# Rename directories
os.rename('demo.txt', 'Example1.txt')
print(os.listdir())

# Look at stat
print(os.stat('Example1.txt'))

# Look at datetime
print('-----------')
mod_time = os.stat('Example1.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# Print all directories and files of the path
for dirpath, dirnames, filenames in os.walk('/Users/hugotorche/Data/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# Manipulate directories with environ
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# Check if a file exists
print(os.path.exists('/tmp/test.txt'))

# Manipulate files
print(os.path.splitext('/tmp/test.txt'))
