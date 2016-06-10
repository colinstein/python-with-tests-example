# An Example Program
Take a look at the [myadder.py](myadder.py) to see the program that we wrote. It
doesn't do very much but we can use it as an example to figure out how we can
make it more useful to more people.

Once you've seen what it does, consider the readme file below. You should try
to always have a readme file like this to explain to people how it works and
what additional setup might be required to make it work.

Your readme doesn't have to be complicated, it just needs to hit the major
points so that a new person will know what it does and how to use the program
the first time they see it.

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
