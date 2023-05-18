# function with parameter
# example 1
def course_func(name, age):
    print('my name is', name, '1 am', age, 'yrs old')


course_func('Richard', 87)

# example2


def my_credentials(name, address, birthdate):
    print("Hello", name, "welcome to compudemy")
    print("I live in", address)
    print("i was born on", birthdate)


my_credentials('Richard', 'allison st mount rainier md', '5/13/1991')

# example 3


def checkeven_odd(m):

    if (m % 2) == 0:
        print(m, "is even number")
    else:
        print(m, "is odd number ")


# call function
checkeven_odd(9)

# example 4 checking divisibility of two parameter


def checkDivisibility(x, z):
    if x % z == 0:
        print(x, " is divisible by ", z)
    else:
        print(x, "is not divisible by ", z)


# call fuction
checkDivisibility(5, 2)
