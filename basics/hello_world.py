# This programs says hello and asks for my name.

print('Hello World!')
print('What is your name?')
my_name = input() # waits for input
print('It is good to meet you, ' + my_name)
print('The length of your name is:' + str(len(my_name)))
print('What is your age?') # asks for their age
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
