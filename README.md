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

## Running Tests
The standard unit testing framework is used so that you can run tests like this:

    $ python -m unittest discover

Altneratively, you can run tests for a specific library by specifying it:

    $ python -m unittest discover adder

