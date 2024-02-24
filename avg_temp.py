from array import *
days = int (input ("How many days do you want to calculate? "))
temp_arr = array('i')
for i in range(days):
    temp = int (input ("Highest temp for day " + str(i + 1) + " is? "))
    temp_arr.append(temp)

avg = sum(temp_arr) / (len(temp_arr))
print ("Average = " + str(avg))

res = sum(i > avg for i in temp_arr)

print ("Average temp is higher than " + str(res) + " days!")
