
def multiply(value):
    result = 1
    for x in value:
        result *= x
    return result
print(multiply((8,2,3,-1,7)))


def addition(value):
    sum = 1
    for x in value:
        sum += x
    return sum
print(addition((8,2,3,0,7)))


x = int(input('Enter the number: '))
y = int(input('Enter the number: '))
z = int(input('Enter the number: '))
def small():
    if x <= y and x <= z:
        a = x 
    elif y <= x and y <= z:
        a = y 
    else:
        a = z
    print('The smallest number among the three is: ', a)
small()


x = int(input('Enter the number: '))
def fizz_buzz():
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
fizz_buzz()


def value(name,age):
    print(f'The name is {name} and the age is {age}')
value('Prasanna',19)


x = int(input('Enter the number: '))
y = int(input('Enter the number: '))
z = int(input('Enter the number: '))
def greater():
    if x >= y and x >= z:
        s = x
    elif y >= x and y >= z:
        s = y
    else:
        s = z
    print('The greatest number among the three numbers is: ',s)
greater()


def fun(digit):
    x = [ ]
    for i in digit:
        if i % 2 == 0:
            x.append(i)
    return x
print('The even number is: ',fun([1,2,3,4,5,6]))


def fun(digit):
    x = []
    for i in digit:
        if i % 2 != 0:
            x.append(i)
    return x
print('The odd number is: ',fun([1,2,3,4,5,6]))


def fun(digit):
    if digit == 1:
        return 'it is not a prime number'
    elif digit == 2:
        return 'it is a prime number'
    else:
        for i in range(2,digit):
            if digit % i == 0:
                return 'it is not a prime number'
        return 'it is prime numbers'
print(fun(4))


def reverse(str):
    x = ''
    for i in str:
        x = i + x
    return x
str = 'Prasanna'
print('The original string is:',str)
print('The reverse_str string is:',reverse(str))


def fun(name,age):
    print(f'Name : {name} Age : {age}')
fun('Prasanna Thapa',19)


def func1(*x):
    for i in x:
        print(i)
func1(2,5,7,3,7)


def calculation(x,y):
    add = x + y
    sub = x - y
    return add , sub
solve = calculation(14,12)
print(solve)


def show_employee(name,salary = 9000):
    print(f'Name:{name} Salary: {salary}')
show_employee('Prasanna',150000)


x = [4,6,8,24,12,2]
print(max(x))


x = [4,6,8,24,12,2]
print(min(x))


rollno = int(input('Enter the number: '))
def info(rollno):
    x = [3,45,23,7,34,1]
    if rollno in x:
        print(f'The roll number {rollno} is present')
    else:
        print(f'The roll number {rollno} is absent')
info(rollno)


x = int(input('Enter the number: '))
def fun(x):
    if x %2 == 0:
        print(f'{x} is the even number')
    else:
        print(f'{x} is the odd number')
fun(x)


x = input('Enter element/word: ').lower()
def ele(x):
    vowel = 0
    consonant = 0
    for i in range(len(x)):
        if x[i] in ['a','e','i','o','u']:
            vowel += 1
        else:
            consonant += 1
    print('The element positon of vowel is',vowel)
    print('The element positon of consonant is',consonant)
ele(x)


value = int (input('Enter a number: '))
def factorial(value):
    x = 1
    while value != 0:
        x *= value
        value = value - 1
    print ('The factorical is:',x)
factorial(value)


x = input('Enter a string: ')
def upperString(x):
    z = x.upper()
    print (z)
upperString(x)


x = input('Enter a string: ')
def lowerString(x):
    y = x.lower()
    print (y)
lowerString(x)




x = int(input('Enter the radius: '))
def findArea(x):
    area = 3.14*x*x
    return area
print('The area of circle is:',findArea(x))