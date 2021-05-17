

# dictionary variable
person = {'name': 'Jenn', 'age': 23}

# The below code is a difficult way to concatenate strings using + operator
# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


# {} braces are placeholders and format() function arguments are the values we want to pass to the placeholders.
# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

# This is more useful when you want placeholders values to be repeated
# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


# You can also pass variables as placeholder values in format function 
# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


# You can also access the placeholder values directly from the dictionary variable below:
# sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
# print(sentence)

# A much better way to write the above code is as below. 
# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print(sentence)

# list variable
# l = ['Jenn',23]

# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
# print(sentence)

# ================== Class definition and instance execution
# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', '33')


# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

# ================== Class execution ends

# Another way to pass dictionary values directly without a variable; more readable
# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)


# Most readable and efficient way to print out dictionary value
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)


# In this example we want to pad 0 to single digit numbers using format method
# for i in range(1, 11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)


# Let's look at how to format decimal values. colon: is an indicator that we want to format something. 
# .3f is formatting to 3 decimal places
# pi = 3.14159265

# sentence = 'Pi is equal to {:.3f}'.format(pi)
# print(sentence)

# Print a large number with comma separators and with 2 decimal places at the endso its more readable. Use :, to indicate comma seperator and .2f for 2 decimal places
# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)


# print out datetime values. Ex: logs, reports
import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
