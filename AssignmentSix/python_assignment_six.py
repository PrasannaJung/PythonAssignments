
def aag(*x):
    print(x)
aag(10,20)


# outer function
def fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = fun(5, 10)
print(result)


def student(name, age):
    print(name, age)

# call using original name
student("Emma", 26)

# assign new name
showStudent = student
# call using new name
showStudent("anna", 26)


x=[1,2,3,4,5,6,7,8]
print(max(x))


# In Python ** is an exponential operator.
# The double asterisk form of **kwargs is used to pass a keyword, 
# variable-length argument dictionary to a function.


# Global variables are those which are not defined 
# inside any function and have a global scope whereas 
# local variables are those which are defined inside a function and 
# its scope is limited to that function only.


x = int(input('Enter the number:\n'))
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


def speed_check(speed):
    global warning_point
    max_speed = 70
    if speed <= max_speed:
        print ("OK")
    elif speed >= max_speed +10:
        print ("Warning")
    else:
        pass
speed_check(67)
speed_check(90)

i = 0
x = int(input('Enter the number:\n'))
for i in range(1,11):
    print(x,'*',x[i],'=',x*x[i])


x = 'parameter'
print(len(x))


def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


a = [8,2,3,-1,7]
multiply =1

for j in a:
   multiply *= j
print(multiply)


x = [8, 2, 3, 0, 7]
sum = 0

for m in x:
    sum += m
print(sum)


x = input('Enter the string:\n')
even = []
odd = []
el = 0
for el in range(len(x)):
    if i % 2 == 0:
        even.append(x[i])
    else:
        odd.append(x[i])
print('even character',even)
print('odd character',odd)


i=1
sum = 0
while i <11:
    sum += i
    i += 1
print(sum)


def num(l):
    enum = []
    for i in l:
        if i % 2 == 0:
            enum.append(i)
    return enum
print(num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def num(l):
    onum = []
    for i in l:
        if i % 2 != 0:
            onum.append(i)
    return onum
print(num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


x = int(input('Enter the number:\n'))
if x < 41:
    print('Failed')
elif x >= 41 and x < 55:
    print('Fair')
elif x >= 55 and x < 65:
    print('Good')
elif x >= 65:
    print('Excellent')
else:
    pass


x = int(input('Enter the number:\n'))
print(str(x)[::-1])
