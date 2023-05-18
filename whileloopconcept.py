# python program to illustrate while loop

count = 1  # mean it start printing from 1 if you put count = 0 it will start printing from 0
# while (count < 3):
# count = count+1
# print('Hey Happiness')

while (count < 5):
    count += 1
    print('Hey Happiness welcom')

# happi = 1
# while (happi < 5):
    # print(happi)
# printing in decending order from 10 to 0 not from 0 to 10
count = 11
while count >= 1:
    count -= 1
    print(count)

# 3 conditions:print even and odd numbers between 1  and 10 to the entered number while loop
nu = 10
# while nu > 0:
# if nu % 2 == 0:
# print(nu, "is even")
# else:
# print(nu, "is odd")
# nu = nu-1
# conditions:print even and odd numbers between 1  and 10 to the entered number using for loop
# for i in range(1, 11):
# if i % 2 == 0:
# print(i, "is even number")
# else:
# print(i, "odd number")

# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list
sum = 0
for i in range(1, 11):
    sum = sum-i
print('the sum of the even number is:', sum)


# Write a Python program that uses a while loop to repeatedly prompt the user to enter positive numbers, and stops when the user enters -1
sum = 0
while True:
    num = int(input("enter a positive number or enter -1 to exit"))
    if num == -1:
        break
    if num > 0:
        sum = sum+num
    else:
        print("invalid input enter a positive number")
print("the sum of the positive number is :", sum)
