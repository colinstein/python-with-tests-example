# An Example Program
The last thing we need to do is write some automated testing. Testing does three
things for us:

  1. It's another form of documentation that explicitly spells out the behaviour
     of your code to other programmers. It helps to know what is explicitly
     intended affects and which are coincidental.

  2. It makes it easier to verify that you didn't break your code when making
     changes. Good tests will check the full set of functionality in your code
     so you can be confident you didn't accidentally break them.

  3. It lets you write code more quickly. An automatic test can verify your code
     much more quickly than manual tests which means you get work done faster.

To write tests all we did was add the [adder/test_adder.py](adder/test_adder.py)
file and define a few cases. The basic idea is to call the methods in your
library with various inputs and ensure you get the expected outputs. If you
expect the method to fail in certain ways (like adding two strings) then write
a test that ensure the failure happens. The unittest framework is part of Python
so the [official documentation for Python Unittest](https://docs.python.org/2.7/library/unittest.html)
is worth taking a look at.

In our sample test we check the 'happy path' (add two numbers), the a mostly
clean path (number and string that can be made a number), and an 'ugly' path
(two strings). We also test negative numbers work and that rational numbers
are rounded off (always floored) and added too.

Some things should always fail. "strings" that can't be added if they can't be
converted into integers so in those cases we ensure that an exception is raised.
Testing for failures is how other programmers will know that sometimes a 'crash'
is expected. Crashing isn't always bad: it prevents your program from having
undefined behaviour which may cause it to compute invalid results or worse:
destroy the computer or data on it.

The nice part about writing our test this way is that there's a standard way to
test run them:

    $ python -m unittest discover

That will automatically find and run all tests. When you import a library that
you have used in the past you can use it to verify that it works. When you make
changes you can run the tests to ensure your program still works correctly. When
you are unsure how to use a library or how it will behave in some edge-case you
can read the tests to see what it is supposed to do.

Tests are awesome.  They're so good we also updated our readme to tell everyone
how they can run the tests that we wrote.

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

## Running Tests
The standard unit testing framework is used so that you can run tests like this:

    $ python -m unittest discover

Altneratively, you can run tests for a specific library by specifying it:

    $ python -m unittest discover adder

