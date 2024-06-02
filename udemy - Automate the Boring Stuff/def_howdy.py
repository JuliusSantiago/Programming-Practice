def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('last Howdy!')

# Executes the method which has 3 print statements.
hello()


# When hola method is called it will print out the string and the concatenated argument.
def hola(name):
    print('Hola ' + name)

hola('Alice')
hola('Bob')


# Executes the method to add one and assigns it to a variable. New number is printed.
def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)
