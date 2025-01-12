#Sequences
#Sequences are a family of built-in types, including the list, tuple, range, string, and binary types.
#Sequences represent ordered and finite collections of items.

#SEQUENCE OPERATIONS
#There are many operations that work across all of the types of sequences. We cover some of the most commonly used
#operations here. You can use the in and not exists in a sequence:

a = 2 in [1,2,3]
print(a)

b = 'a' not in 'cat'
print(b)

c = 'u' in 'Sugar'
print(c)

d = 10 in range(12)
print(d)

e = 10 not in range(2,6)
print(e)

#You can reference the contents of a sequence by using its index number. To access the item at some index,
#use square brackets with the index number as an argument. The first item indexed is at position 0, the second
#at 1, and so forth up to the number one less than the number of items:

my_sequence = 'Bill Clinton'
print(my_sequence[0])
print(my_sequence[1])
print(my_sequence[8])

#Indexing can appear from the end of a sequence rather than from the front using negative numbers.
#The last item has the index of –1, the second to last has the index of –2, and so forth:

print(my_sequence[-1])
print(my_sequence[-2])
print(my_sequence[-12])

#The index of an item results from the index method. By default, it returns the index of the first occurrence
#of the item, but optional arguments can define a subrange in which to search:

print(my_sequence.index('B'))
print(my_sequence.index('l'))
print(my_sequence.index('l',5,13))

#You can produce a new sequence from a sequence using slicing. A slice appears by invoking a sequence with brackets
#containing optional start, stop, and step arguments:

    #my_sequence[start:stop:step]

#start is the index of the first item to use in the new sequence, stop the first index beyond that point, and step,
#the distance between items. These arguments are all optional and are replaced with default values if omitted.
#This statement produces a copy of the original sequence. The default value for start is 0, for stop is the length
#of the sequence, and for step is 1. Note that if the step does not appear, the corresponding : can also be dropped:

vowels = ['a','e','i','o','u']
print(vowels[2:4])
print(vowels[:3])
print(vowels[2:])

#Negative numbers can be used to index backward:
print(vowels[-1:])
print(vowels[-6:-1])

#Sequences share many operations for getting information about them and their contents. len returns the length
#of the sequence, min the smallest member, max the largest, and count the number of a particular item.
#min and max work only on sequences with items that are comparable. Remember that these work with any sequence type:

print(len(vowels))
print(max(vowels))
print(min(vowels))

