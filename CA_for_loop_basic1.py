# 1. Basic - Print all integers from 0 to 150.
print("Answer to question number 1 - Basic")
for i in range(150):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Answer to question number 2 - Multiples of Five")
for i in range(5, 1000, 5):
    print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
#    print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Answer to question number 3 - Counting, the Dojo Way")
for integer in range(1,100):
    if integer%10 == 0:
        print("Coding Dojo")
    elif integer%5 == 0:
        print("Coding")
    else:
        print(integer)

# 4. Add odd integers from 0 to 500,000, and print the final sum.
print("Answer to question number 4 - Add odd integers from 0 to 500,000")
final_sum=0
for integer in range(1, 5000000, 2):
    final_sum += integer
if final_sum > 0:
    print("final sum is", final_sum)
else:
    print("final sum is 0")

# 5. Countdown by Fours - 
#    Print positive numbers starting at 2018, counting down by fours.
print("Answer to question number 5 - Countdown by Fours")
for integer in range(2018,0,-4):
    if integer > 0:
        print(integer)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. 
#    Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
#    For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("Answer to question number 6 - Flexible Counter")
lowNum = 3
highNum = 100
mult = 3
for integer in range(lowNum,highNum,3):
    print(integer)




