#Handling Exceptions
#Exceptions are a type of error causing your program to crash if not handled (caught).
#Catching them with a try-except block allows the program to continue.
#These blocks are created by indenting the block in which the exception might be raised,
#putting a try statement before it and an except statement after it, followed by a code block that should run
#when the error occurs:

planets = ['Venus','Jupiter','Mercury','Saturn']
while True:
    try:
        planet = planets.pop()
        print(planet)
    except IndexError as e:
        print("We tried to pop too many planets")
        print(e)
        break

#There are many built-in exceptions, such as IOError, KeyError, and ImportError.
#Many third-party packages also define their own exception classes. They indicate that something has gone very wrong,
#so it only pays to catch them if you are confident that the problem won’t be fatal to your software.
#You can specify explicitly which exception type you will catch. Ideally, you should catch the exact
#exception type (in our example, this was the exception IndexError).

