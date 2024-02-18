print('Enter a name.')
name = input()
if name:    # truthy if there is an input, falsey if there is no input
    print('Thank you for entering a name. ' + name + '.')
else:
    print('You did not print a name.')

# int 0 is falsey, all other values truthy
# float 0.0 is falsey, all other values truthy
# empty string ' ' is falsey, else it is truthy
