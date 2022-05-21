
# while True:
#    userInp = input('Enter a vowel letter: ')
#    vowels = ['a','e','i','o','u']
#    if userInp in vowels:
#       print('It\'s a vowel')
#       break
#    else:
#       print('Please try again')
#       pass
   
# i = 0
vowels = ['a','e','i','o','u']

# while (i == 0):
#    userInp = input('Enter a vowel letter: ').lower()
#    if userInp in vowels:
#       print('It is a vowel')
#       i+=1   
#    else:
#       print('Please give a vowel input')

      
userInp = input('Enter a vowel letter: ').lower()

while userInp not in vowels:
   userInp = input('Enter a vowel letter: ').lower()
   
   