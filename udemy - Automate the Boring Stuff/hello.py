# This program says hello and asks for my name

print('Hello world!')
print('What is your name?') # ask for their name
myName = input() # prompts user for input
print('It is good to meet you ' + myName)
print('The length of your name is: ')
print(len(myName)) # prints out length of myName string
print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # concatenates string + value + string

# string concatenation does only all strings
# input() will output a string
# len() to get integer length value
# str(), int(), float() converts to that data type, aka Casting
# print() for displaying value passed to it