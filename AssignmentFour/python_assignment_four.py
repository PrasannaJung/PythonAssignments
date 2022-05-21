
i = 2
while i<15:
        print(i)
        i += 2
   
 
i =1 
while i<21:
    print(i)
    i += 2
    

i=1
while i <11:
    print (i)
    i += 1
    

x = 'python'
b = ''
i = len(x)-1
while(i>=0):
    b = b+ x[i]
    i -= 1
print(b)


a = [1, 2, 3, 4]
b = []
i = len(a)-1
while(i>=0):
    b.append(a[i])
    i -= 1
print(b)


a = [1, 2, 3, 4]
i = len(a)-1
while(i>=0):
    print(a[i])
    i -= 1 
 



a = [1, 2, 3, 4]
sum =1
i = 0
while(i<len(a)):
    sum *= a[i]
    i += 1
print(sum)



for i in range(1,31):
    print(i*10)


i = 105
while(i >= 7):
    print(i)
    i -= 7
    



x = int(input('Enter the number: '))
factorical = 1
if x < 0:
    print('Sorry the number does not exist for negative value')
elif x == 0:
    print('The factorical of 0 is 1')
else:
    for i in range(1, x+1):
        factorical = factorical*i
    print('The factorical of',x,'is',factorical)
    
    