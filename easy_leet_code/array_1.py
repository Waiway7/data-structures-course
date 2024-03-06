from array import *

# 1. create an array and tranverse

my_array = array("i", [1,2,3,4])

for i in (my_array):
    print (i)

# 2. access individual elements through indexes
# print ("step 2")
print (my_array[0])

# 3 append any value to the array using append() method
my_array.append(5)
# print (my_array)

#4 insert value in an array using insert() method

my_array.insert(2, 5)


#5 extend array using extend() method
my_array1 = array("i", [10,11,12])
my_array.extend(my_array1)
# print (my_array)

#6 add items from list into array from using fromlist() method
my_array.fromlist([12,13,14])
# print (my_array)

#7 remove any ele from array
my_array.remove(12)
# print (my_array)

#8 remove last array element using pop() method
my_array.pop()
# print (my_array)

#9 fetch any element through its index using index method
print (my_array.index(5))

#10 reverse pythona array
my_array.reverse()
print (my_array)

#11 get array buffer through buffer_info() method
print (my_array.buffer_info())

#12 check for number of occurances of an element using count() mehtod
print (my_array.count(5))
#12 convert array to string using tostring() method
