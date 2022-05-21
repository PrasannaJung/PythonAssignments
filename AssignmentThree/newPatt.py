for i in range(1,6):
   for j in range(1,i+1):
      if(i==j):
         print(i*8,end=' ')
      if((i+1)%2==0):
         if(j%2==0):
            print(0,end =' ')
      if((i+1)%2!=0):
         if(j%2!=0):
            print(0,end =' ')
   print()   