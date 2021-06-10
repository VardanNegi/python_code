import csv


""" This is an example of reading a csv and writing to a new file
# The reader method expects a csv dialect to read, by default it expects a csv file to be seperated by a comma.
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	# copy csv to a new_file With context manager
	with open('new_names.csv','w') as new_file:
		# To put deilimter as - 
		#csv_writer = csv.writer(new_file, delimiter ='-')
		csv_writer = csv.writer(new_file, delimiter ='\t')

		# reading each row from names.csv and writing rows to new_names.csv
		for line in csv_reader:
			csv_writer.writerow(line)

Example ends """

""" open new_file which is tab delimited we just created from above block of code. To read this file properly put delimiter in reader method as -
with open('new_names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter ='\t')

	for line in csv_reader:
		print(line)
Example end """


"""# Using dictionaries to read and write csv. We can get the email easily. would be difficut to extract info if csv is too large and would have to open
# the csv file manually to check the position of the filed to extract.

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	
	with open('new_names.csv','w') as new_file:
		
		fieldnames = ['first_name','last_name','email']
		csv_writer = csv.DictWriter(new_file,fieldnames = fieldnames, delimiter ='\t')

		csv_writer.writeheader()

		
		for line in csv_reader:
			csv_writer.writerow(line)

Example ends"""

 # If you dont want to include email field here's the code

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	
	with open('new_names.csv','w') as new_file:
		
		fieldnames = ['first_name','last_name']
		csv_writer = csv.DictWriter(new_file,fieldnames = fieldnames, delimiter ='\t')

		csv_writer.writeheader()

		
		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)
























