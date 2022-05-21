
a = 7
b = 9
if a == b:
    print('1')
elif a>b:
    print('2')
else:
    print('3')



a = 1
b = 1
c = 2
d = 2
if a == b and c == d:
    print('Hello')



a = 10
b = 22
c = 5
d = 5
if a == b or c == d:
    print('Hello')
else:
    print('Does not exist')



x = int(input('Enter a number: '))
if x > 0:
    print('True')
elif x < 0:
    print('False')
else:
    print('Zero')



userInpNum = float(input('Enter the number: '))
if userInpNum % 2 == 0:
    print('It is even.')
else:
    print('It is odd.')



subOne = float(input('Enter the marks of math: '))
subTwo = float(input('Enter the marks of science: '))
subThree = float(input('Enter the marks of computer: '))
subFour = float(input('Enter the marks of english: '))

totalMarks = 400
marksAchieved = subOne + subTwo + subThree + subFour

totalPercentage = ( marksAchieved / totalMarks ) * 100

if totalPercentage >= 70:
    print('You got distinction')
    Grade = 'A'
elif totalPercentage >= 60:
    print('You got first division')
    Grade = 'B'
elif totalPercentage >= 40:
    print('Passed')
    Grade = 'C'
else:
    print('Failed')
    Grade = 'E'

print('Your marks is:', marksAchieved)
print('Your percentage is:', totalPercentage,'%')
print('Your grade is:', Grade)




print('APPLE'>'apple')


print("Personal details")
myName = 'Prasanna Jung Thapa'
myAge = 19
myAddress = 'Kathmandu'
print(myName)
print(myAge)
print(myAddress)

 

PI = 22/7
r = float(input('Enter the radius of the circle:(in m): '))
Area = PI * (r**r)
print(f'The area of circle is {Area} m²')



a = int(input('Enter the no of students in class a: '))
b = int(input('Enter the no of students in class b: '))
c = int(input('Enter the no of students in class c: '))
print('The possible no of desk that can be purchase is:')
print(a//2 + a%2 + b//2 + b%2 + c//2 + c%2) 



a = int(input('Enter the number: '))
b = int(input('Enter the number: '))
c = int(input('Enter the number: '))
if a >= b and a<= c:
    print(b)
elif b >= c and a <= c:
    print(a) 
else:
    print(c) 
  


a = int(input('Enter the number: '))
b = int(input('Enter the number: '))
c = int(input('Enter the number: '))
print(a + b + c)



x = int(input('Enter the height of right angled triangle: '))
y = int(input('Enter the length of base: '))
print(x * y /2)


students = int(input('Number of students: '))
apples = int(input('Number of Apples: '))
print(apples // students)
print(apples % students)




a = 'banana'

print(a.upper())













