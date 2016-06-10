# An Example Program
Now we've actually done the extraction of our method into a reusable library.
You can find the method in [adder/adder.py](adder/adder.py), we just cut and
pasted it over there. If you had a bunch of related methods you could put them
all into that file. For example, you might have an `addFloat()` or `addHex()`
method in that file too. Try to group related methods into one file.

We also added [adder/__init__.py](adder/__init__.py) which pulls in the rest of
our library in. You can treat this as boilerplate. Just add one line (like the
first) for each file in the folder that contains code you want to include.

The `adder` folder is now a library that we could easily pull into other
programs. If you find yourself writing similar functionality in multiple
programs, you might want to pull this library out into it's own repository. We
don't have to do that now, but if you'd like to then just ask for help.

We modified [myadder.py](myadder.py) to so that it calls the library we created
and calls our `addI()` method within it.

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
