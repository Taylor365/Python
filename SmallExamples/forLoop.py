print('My name is')
for i in range(5):
    print('Jimmy Five Times  (' + str(i) + ')')
    
total = 0
for num in range(101):
    total = total + num
print(total)

#First int starts, second is up to but not including e.g.:
for i in range(12, 16):
    print(i)

#The third is the step int (increase by) e.g.:
for i in range(0, 10, 2):
    print(i)

#Prints from 5 down to 0
for i in range(5, -1, -1):
    print(i)
