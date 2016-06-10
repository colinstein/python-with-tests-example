#!/usr/bin/env python
from sys import argv
import adder

""" This is our main entry point, it handles extracting parameters and """
""" ensuring that they get passed on to our 'worker' method. """
def main():
  if len(argv) < 3:
    sys.stderr.write("Bad Usage. Try {} 2 9\n".format(argv[0]))
    exit(1)
  try:
    oppSum = adder.addI(argv[2], argv[1])
    print("The sum of {} and {} is {}.".format(argv[1], argv[2], oppSum))
  except ValueError:
    sys.stderr.write("Both arguments must be integers.\n")
    exit(1)

if __name__ == "__main__":
  main()
