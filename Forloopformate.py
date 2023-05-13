#loop in python
# for loop
for num in range(1, 10):  # it will print from 1 to 9 and just (10) will be from 0 to 9
    print(num)

# example2 for loop with strings
name = "Happiness"
for i in name:
    print(i)

# example3 looping with list
student = ['akum', 'happiness', 'richard', 'mary', 'elizabeth']
ages = [1, 2, 3, 4, 5]
for i in student:
    print(i)
for i in ages:
    if i == 4:
        print('hey welcom')
    else:
        print('welcom')

# example4

# it will print from 1 to 20 but if you put just(21) it will print from 0 to 20
for num in range(1, 21):
    print(num)

# performing sum of first 10 number using for loop(0 to 9)
sum = 0
for i in range(1, 10):
    sum = sum+i
print('the sum of the number is:', sum)

# example5

# performing sum of first 21 number using for loop(1 to 20)
sum = 1
for i in range(1, 21):
    sum = sum+i
print('the sum of the number is:', sum)
