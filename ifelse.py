a = 45
if a == 45:
    print("a is 45")

#Here we use the == operator, which return True if items are equal and False if not.
#Optionally, this block can follow an elif or else statement with an accompanying block.
#In the case of an elif statement,this block only executes if the elif evaluates to True:

b=30
if b == 100:
    print("b is 100")
elif b == 30:
    print("b is 30")

#Multiple elif loops can append together. If you are familiar with switch statements in other languages,
#this simulates that same behavior of choosing from multiple choices. Adding an else statement at the end
#runs a block if none of the other conditions evaluate as True:

c=0
if c == 1:
    print("c is 1")
elif c == 2:
    print("c is 2")
elif c > 10:
    print("c is greater than 10")
elif c < 10:
    print("Value of c is less than 10,  Actual value of c is :",c)
else:
    print("I don't know much about c")

#You can nest if statements, creating blocks containing if statements that
#only execute if an outer if statement is True:

cat = 'spot'
if 's' in cat:
    print("Found an 's' in cat")
    if cat == 'shera':
        print("i found shera")
    else:
        print("Some other cat")
else:
    print("No 's' found in cat")


