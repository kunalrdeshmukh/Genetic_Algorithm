# Kunal Deshmukh + Eric Tjon

import random
import re


def nucleotide(n):
  if n == 0:
    return 'A'
  elif n == 1:
    return 'T'
  elif n == 2:
    return 'C'
  elif n == 3:
    return 'G'


def different(notn):
  n = random.randint(0,3)
  if nucleotide(n) == notn:
    n = (n + random.randint(1,3))%4
  return nucleotide(n)


def mutate(sequence, mutation, n=None):
  length = len(sequence)
  pos = random.randint(0,length-1)

  if mutation == 'M':
    return sequence[:pos] + different(sequence[pos]) + sequence[pos+1:]

  elif mutation == 'N':
    #Taken from stackoverflow
    sub_index = [m.start() for m in re.finditer('AG', sequence)]
    pos = random.choice(sub_index)
    return sequence[:pos] + 'T' + sequence[pos:] 

  elif mutation == 'I':
    return sequence[:pos] + different('x') + sequence[pos:]

  elif mutation == 'D':
    return sequence[:pos] + sequence[pos+1:]

  elif mutation == 'U':
    return sequence[:pos] + sequence[pos:pos+n] + sequence[pos:] 
  elif mutation == 'R':
    return sequence[:pos] + sequence[pos:pos+n] * n + sequence[pos:]

