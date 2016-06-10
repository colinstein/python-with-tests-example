# An example program
After reading our test cases we discover our readme is out of date. Testing
forced us to consider the 'floating point' or 'rational number' case and we
decided to handle it. We should update our documentation because it says they
do not work and that isn't true.

---

# My Adder
This program adds two numbers. You pass in some integegers as command line
arguments and it'll tell you what the sum of them is with plane English.

It will add floating point numbers by 'flooring' them (3.999 turns into 3, not
4), but will only add base-10 numbers, not hexidecimal or complex numbers, nor
numbers in some other strange base. Negative numbers are correctly handled too.

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

## Running Tests
The standard unit testing framework is used so that you can run tests like this:

    $ python -m unittest discover

Altneratively, you can run tests for a specific library by specifying it:

    $ python -m unittest discover adder

