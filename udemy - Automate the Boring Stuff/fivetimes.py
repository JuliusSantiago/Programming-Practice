print('My name is ')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

total = 0
for num in range (101): # for loop 0 - 100 is implied
    total = total + num
print(total)

print('My name is ')
j = 0
while j < 5:
    print('Jimmy While Five Times ' + str(j))
    j = j + 1
    if j == 5:
        break

print('Range is ')
for k in range(4, 16, 2):  # 4 to 16, step up +2, can also use negative
    print('now ' + str(k))
