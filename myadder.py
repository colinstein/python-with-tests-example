#!/usr/bin/env python
import sys

if len(sys.argv) < 3:
  sys.stderr.write("Bad Usage. Try {} 2 9\n".format(sys.argv[0]))
  exit(1)

try:
  oppA = int(sys.argv[1])
  oppB = int(sys.argv[2])
except ValueError:
  sys.stderr.write("Both arguments must be integers.\n")
  exit(1)

oppSum = oppA + oppB

print("The sum of {} and {} is {}.".format(oppA, oppB, oppSum))
