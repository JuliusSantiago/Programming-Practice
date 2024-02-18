spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue    # immediately return to beginning of while loop
    print('Spam is ' + str(spam))

# This should skip 'Spam is 3' because of the continue statement
