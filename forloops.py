#for loops allow you to repeat a block of statements (a code block) once for each member of a sequence
#(ordered group of items). As you iterate through the sequence, the current item can be accessed by the code block.
#One of most common uses of loops is to iterate through a range object to do a task a set number of times:

for a in range(10):
    b = a*2
    print("b is ", b)
#We repeat this code 10 times, each time assigning the variable i to the next number in the sequence of integers
#from 0–9. for loops can be used to iterate through any of the Python sequence types.

#CONTINUE
#The continue statement skips a step in a loop, jumping to the next item in the sequence:

for c in range(5):
    if c == 2:
        continue
    print("C is ",c)
#In the output all the value from 0 to 5 will be printed except 2 which will be skipped.



