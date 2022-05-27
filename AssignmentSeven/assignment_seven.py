import random
# To get the smallest number in a list
list_one = [1,2,3,4,5]
print(min(list_one))

# Function to check if a list is empty
empty_list = []

def check_empty(my_list):
    if len(my_list) == 0:
        return 'Empty'
    else:
        return 'Not Empty'
print(check_empty(empty_list))     

# To select random element from a list
print(random.choice(list_one))

# Program to copy a list
to_be_copied = [1,2,3]
copied_list = to_be_copied.copy()
print(copied_list)

# Find the second largest number in a list
second_largest = [2,3,4,5,6]
second_largest.sort()
print(second_largest[-2])

# Count the number of even and odds from a sequence of numbers
our_numbers = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
odd_count = 0

for i in our_numbers:
   if i%2==0:
      even_count += 1
   else:
      odd_count += 1
print(even_count)
print(odd_count)      

# Add an element to a tuple
original_tuple = (1,2,3)
converted_tuple = list(original_tuple)
converted_tuple.append(4)
changed_tuple = tuple(converted_tuple)
print(changed_tuple)

# convert a tuple to list
tuple_to_convert = (1,2,3)
to_list = list(tuple_to_convert)

# convert tuple to string
to_string = str(tuple_to_convert)

# convert a list to tuple
new_tuple = tuple(to_list)

# convert list of tuple to dictionary
user_list = [('name','John'),('age',25)]
user_data_dict = dict(user_list)

# add a key to a dictionary
sample_dict = {0:10,1:20}
sample_dict[2] = 30

# concatenate the given dictionaries
dict_one = {1:10,2:20}
dict_two = {3:30,4:40}
dict_three = {5:50,6:60}

dict_one.update(dict_two)
dict_one.update(dict_three)

# check if a key is in a dictionary
key_check_dict = {
   'name':'Prasanna',
   'age':19
}
if 'name' in key_check_dict:
   print('Yes it is')
else:
   print('No it is not')
   
# print a dictionary where the keys are the numbers from 1 to 15 and the values are square of the keys
square_dict = {}

for i in range(1,16):
   square_dict[i] = i**2   
   
# merge two python dictionaries
first_dict = [1,2]
to_be_merged = [3,4]
first_dict.extend(to_be_merged)

# find third largest number in a list
third_largest_list = [4,5,6,7,8,9]
third_largest_list.sort()
print(third_largest_list[-3])

# creating a set
our_set = {'a','b','c','d','e','f'}

# iterating over the set  
for el in our_set:
   print(el)
   
# add members to a set
our_set.add('g')

# remove item from a set
our_set.discard('a')

# remove an item from a set if it is present in the set
our_set.remove('a')

# create intersection of sets

setOne = {1,2,3,4,5}
setTwo = {4,5,6,7,8}

intSets = setOne & setTwo

# check if a value exists inside a dictionary
my_dict = {'a':1,'b':2,'c':3}

if 1 in my_dict.values():
   print('Yes')


