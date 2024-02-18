## try and except statement so that the program will
## continue running, but will output another statement
## without executing the error
def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:   # input validation
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12)) 
print(div42by(0))
print(div42by(8))


## User input validation
print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 3:
        print('That is a lot of cats.')
    else:
        print('You need more cats.')
except ValueError:
    print('That is not a number.')
    
