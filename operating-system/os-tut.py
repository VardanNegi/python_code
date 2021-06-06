
import os
from datetime import datetime


"""
The OS module allows us to interact wiht the underlying operating system in several different ways.

- Navigate the file system
- Get file information
- Look up and change the environment variables
- Move files around
- Many more

To begin, import the os module. This is a built in module, no third party modules need to be installed
"""

# Get current working directory
# print(os.getcwd())

# navigate to a new file system /Volumes/Macintosh HD - Data/
# os.chdir('/Volumes/Macintosh HD - Data/')
# print(os.getcwd())

# list directories and files in the current path
#print(os.listdir())

# create new folder in path
#os.mkdir('OS-Demo-2/Sub-Dir')
#os.makedirs('OS-Demo-2/Sub-Dir')


# delete folders
# os.rmdir('OS-Demo-2/Sub-Dir')
# os.removedirs('OS-Demo-2/Sub-Dir')
# print(os.listdir())

# stats within a file
# print(os.stat('function.py'))
# # print size and last modified time
# print(os.stat('function.py').st_size)
# mod_time = os.stat('function.py').st_mtime
# convert timestamp to datetime

# print(datetime.fromtimestamp(mod_time))

# list entire directory tree and print the files
# os.chdir('/Volumes/Macintosh HD - Data/')
# for dirpath, dirnames, filenames in os.walk('/Volumes/Macintosh HD - Data/python-code'):
# 	print('Current Path:', dirpath)
# 	print('Directories:', dirnames)
# 	print('Files: ',filenames)

# access env variables

# print(os.environ.get('HOME'))
# file_path = os.path.join(os.environ.get('HOME'),'test.txt') 
# print(file_path)

# some more basics /tmp/test.txt is a fake path does not exist
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

#methods in os.path module
print(dir(os.path))










