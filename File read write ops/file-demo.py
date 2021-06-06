# File Objects

# using context manager. benefit of using with is it will open and close the file automatically
# with open('test.txt', 'r') as f:
	# this is for reading the entire file
	#f_contents = f.read()
	# what if the file is too large? then just read the file using readlines as the lines of contents in file as elements of list
	#f_contents = f.readlines()
	# if you want to read the contents line by line then use readline
	# f_contents = f.readlines()
	# print(f_contents,end ='')
	# # using end does not print \n at the end of the print statment
	# f_contents = f.readlines()
	# print(f_contents,end ='')
	# prints out 
	#print(f_contents)
	# using for loop is efficient in terms of memory the file is not read all at once. It is read one by one.
	# for line in f:
	# 	print(line, end='')


# open the files test.txt in read mode. The file should be in the same python library path as pyton file. 
#f = open('test.txt', 'r')

# print name of the file
#print(f.name)
# print the mode of the file
#print(f.mode)
# this will close the file. not required for now as we are using with 
#f.close()


# with open('test.txt', 'r') as f:
# 	# 100 is for reading first 100 chars
# 	f_contents = f.read(100)
# 	print(f_contents,end ='')

# we are reading 10 characters after every f.read() because it increments from the character it left
# with open('test.txt', 'r') as f:
# 	size_to_read =10
# 	f_contents = f.read(size_to_read)

# 	while len(f_contents) >0:
# 		print(f_contents, end='*')
# 		f_contents = f.read(size_to_read)


# with open('test.txt', 'r') as f:
#  	size_to_read =10
#  	f_contents = f.read(size_to_read)
#  	# prints the current position of read
#  	print(f.tell())


# Writing to file. If file does not exist it will create a new one or if exists it will overide it.

# with open('test2.txt','w') as f:
# 	f.write('Test')

# reading from an existing file and writing to a new file line by line
# with open('test.txt','r') as rf:
# 	with open('test_copy.txt','w') as wf:
# 		for line in rf:
# 			wf.write(line)

# copying a picture in jpeg. Use b with r or b mode to open in binary mode.
# with open('pic_dwld.jpeg','rb') as rf:
# 	with open('pic_dwld_copy.jpeg','wb') as wf:
# 		for line in rf:
# 			wf.write(line)


# instead of doing line by line, we can do it by chunk sizes as well
with open('pic_dwld.jpeg','rb') as rf:
	with open('pic_dwld_copy.jpeg','wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) >0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)










