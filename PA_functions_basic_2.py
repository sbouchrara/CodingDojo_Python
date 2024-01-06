# Create a function that accepts a number as an input. 
# Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
def Countdown(num=3):
    my_list = []
    x = num+1
    while x > 0:
        x -= 1
        my_list.append(x)
    return my_list
number = 20
if number > 0:
    print(Countdown(number))
else:
    print(Countdown())


# Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
def print_and_return(mylist):
    x = len(mylist)
    if x == 2:
        print(mylist[0])
        return mylist[1]
rval=print_and_return([4,2])
print("Second value returned =",rval)


# Create a function that accepts a list and returns 
# the sum of the first value in the list plus the list's length.
def first_plus_length(mylist):
    x = len(mylist)
    if x>0 and mylist[0]>0:
        return x+mylist[0]
rval=first_plus_length([1,2,3,4,5])
print("Sum =",rval)


# Write a function that accepts a list and creates a new list containing only the values
# from the original list that are greater than its 2nd value.
# Print how many values this is and then return the new list.
# If the list has less than 2 elements, have the function return False
def values_greater_than_second(mylist):
    x=len(mylist)
    newlist=[]
    if len(mylist)<2:
        return False
    else:
        for y in range(0,len(mylist)):
            if y<x-1 and mylist[y]>mylist[y+1]:
                newlist.append(mylist[y])
        print("number of values is",len(newlist))
        return newlist
plist=[5,2,3,2,1,4]
newlist=values_greater_than_second(plist)
if newlist == False:
    print("list with less than 2 values")
    
else:
    print("new list =",newlist)


# Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.
def length_and_value(size,value):
    mylist=[]
    for y in range(0,size):
        mylist.append(value)
    return mylist
a=7
b=4
mylist=length_and_value(a,b)
print(mylist)