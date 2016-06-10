# An Example Program
Take a look at the [myadder.py](myadder.py) to see the program that we changed.
In this program we did some minor refactors. The first is that we moved the
"body" of our program into a function called `main()` and then at the very end
that method is called if our program is being run; that's the last 2 lines. That
change helps make the code easier to read becuase it means the "entry point"—or
the first bit of code that gets run—is easily found. This is a convention that
Python programmers will expect you to follow so we do it.

The second thing we did is move our "core logic" (adding two things) into a
function called `addI()` that does the work. There's still a bit of code for
parsing the command and handling failures but the important bit of our program
is now an isolated unit. We took this step to make our method easier to extract
into a package that can be included in other programs. If you ever need to add
two things together in another program you can just use the package.

We also added some comments to make it a little more clear what our methods do.

---

# My Adder
This program adds two numbers. You pass in some integegers as command line
arguments and it'll tell you what the sum of them is with plane English.

It does not add strings, floating point numbers, numbers that aren't in base-10
or any other weird nonsense. Numbers that are very large (±2 billion) may fail.

## Description
After installing the program you can use it like this:

    $ ./myadder.py 14 7

It will display "The sum of 14 and 7 is 21."

## Requirements
This program should work equally well on Linux and Mac OS X. The dependencies
should be present on any reaosnably popular UNIX-like operating system.

  * Python 2.x

## Zero to Running
All you need to do is clone the repository and run the `./myadder.py` program.
