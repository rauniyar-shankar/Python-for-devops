#Python Variable
#Python Variable is containers that store values. Python is not “statically typed”.
#An Example of a Variable in Python is a representational name that serves as a pointer to an object.
#Once an object is assigned to a variable, it can be referred to by that name.

#Rules for Python variables
#A Python variable name must start with a letter or the underscore character.
#A Python variable name cannot start with a number.
#A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
#Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
#The reserved words(keywords) in Python cannot be used to name the variable in Python.

#an integer assignment
age = 45

#A floating Point
salary = 87500.90

#A string assignment
name = "Shankyy"

print(age)
print(salary)
print(name)
print(age,salary,name)

#Python Datatypes
#Data types are the classification or categorization of data items.
#It represents the kind of value that tells what operations can be performed on a particular data.
#Since everything is an object in Python programming, data types are classes and variables are instances

#(objects) of these classes.

#DataTypes:
            #Numeric:   integer, float, complex number
            #Dictionary:
            #Boolean:
            #Set
            #Sequence Type : Strings, Tuples, List

a = "hello world" #string
b = 100 #integer
c = 60.5 #float
d = 3j #complex number
e = ["python", "for", "devops"] #list
f = ("python", "for", "devops") #tuple
g = {"name":"shankyy", "dob":19960503} #dictionary
h = {"python","for","devops"} #set
i = True #bool
i = b"devops" #binary

print(a,b,c,d,e,f,g,h,i)

#List: Lists are just like dynamic-sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
#Lists need not be homogeneous always which makes it the most powerful tool in Python.
# The main characteristics of lists are –
    #The list is a datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.
    #List are mutable .i.e it can be converted into another data type and can store any data element in it.
    #List can store any type of element.

#Creating a Empty list
List2 = []
print(List2)

# Creating a List of numbers
List3 = [10, 20, 14]
print(List3)

# Creating a List of strings and accessing using index
List4 = ["Python", "For", "Devops"]
print(List4[0])
print(List4[2])

#Tuple: Tuple is a collection of Python objects much like a list.
#The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
#Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary,
#it is more common to define a tuple by closing the sequence of values in parentheses.
#The main characteristics of tuples are –
    #Tuple is an immutable sequence in python.
    #It cannot be changed or replaced since it is immutable.
    #It is defined under parenthesis().
    #Tuples can store any type of element.

# Creating an empty Tuple
Tuple1 = ()
print("\nBlank Tuple",Tuple1)

# Creating a Tuple with the use of list
List5 = [1, 2, 4, 5, 6]
print("\nTuple using List: ", tuple(List5))

# Creating a Tuple with the use of built-in function
Tuple2 = tuple('Python')
print("\nTuple with the use of function: ",Tuple2)

#Set: In Python, Set is an unordered collection of data type that is iterable, mutable, and has no duplicate elements.
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether
#a specific element is contained in the set. The main characteristics of set are –
    #Sets are an unordered collection of elements or unintended collection of items In python.
    #Here the order in which the elements are added into the set is not fixed, it can change frequently.
    #It is defined under curly braces{}
    #Sets are mutable, however, only immutable objects can be stored in it.

# Creating a Empty Set
set1 = set()
print("\nInitial blank Set: ",set1)

# Creating a Set with the use of Constructor (Using object to Store String)
String = 'PythonforDevops'
set2 = set(String)
print("\nSet with the use of an Object: ",set2)

# Creating a Set with the use of a List
set3 = set(["Python", "For", "Devops"])
print("\nSet with the use of List: ",set3)

#List is Mutable and Tuple is not (Cannot update an element, insert and delete elements)
#Tuples are faster because of read only nature. Memory can be efficiently allocated and used for tuples.
#Example for above

_list1 = [1,2,3,4,5,6,7,8,9,0]
_tuple1 = (1,2,3,4,5,6,7,8,9,0)

_list1[3] = 100
#_tuple1[3] = 100 (You will receive error while running this code)

print(_list1)
print(_tuple1)














