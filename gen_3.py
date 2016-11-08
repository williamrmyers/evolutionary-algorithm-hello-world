#!/usr/bin/python3

# This program is a Genetic algorithem program to search find he 
# https://www.electricmonk.nl/log/2011/09/28/evolutionary-algorithm-evolving-hello-world/



# imports
import random
import time



source = "jiKnp4bqpmAbp"
target = "Hello, World!"



# this will evaluate and return the fitness of the string

def fitness(source, target):
   fitval = 0
   for i in range(0, len(source)):
      fitval += (ord(target[i]) - ord(source[i])) ** 2
   return(fitval)


# This funtion mutates the string by pick a random character in the string, and either incrementing or decrementing it by one, or leaving it alon 

def mutate(source):
   charpos = random.randint(0, len(source) - 1)
   parts = list(source)
   parts[charpos] = chr(ord(parts[charpos]) + random.randint(-1,1))
   return(''.join(parts))





# output the results to screen

# print("Source: "+ source)

# print("Target:" + target)

# print("Fitness of source:" + str(fitness(source, target)))


# print('Mutateed Source: ' + mutate(source))

# print('Mutateed score: ' + str(fitness(mutate(source),target)))


fitval = fitness(source, target)
i = 0
while True:
   i += 1
   m = mutate(source)
   fitval_m = fitness(m, target)
   print("%5i %5i %14s" % (i, fitval_m, m))
   if fitval_m < fitval:
      fitval = fitval_m
      source = m
      # print("%5i %5i %14s" % (i, fitval_m, m))
      # Waits a second to slow diplay
      time.sleep(.1)
   if fitval == 0:
      break
