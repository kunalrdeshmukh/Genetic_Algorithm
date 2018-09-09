## Kunal Deshmukh + Eric Tjon

import random
import re

#maps n from 0-3 to a nucleotide
def nucleotide(n): 
  if n == 0:
    return 'A'
  elif n == 1:
    return 'T'
  elif n == 2:
    return 'C'
  elif n == 3:
    return 'G'

#returns a random nucleotide that is different than the argument
def different(notn): 
  n = random.randint(0,3)
  if nucleotide(n) == notn:
    n = (n + random.randint(1,3))%4
  return nucleotide(n)


def mutate(sequence, mutation, n=None):
  length = len(sequence)
  pos = random.randint(0,length-1)
  new_seq = sequence #default value

  if mutation == 'M': #Missense
    new_seq = sequence[:pos] + different(sequence[pos]) + sequence[pos+1:]

  elif mutation == 'N': #Nonsense
    #Taken from stackoverflow to find all substring indicies
    sub_index = [m.start() for m in re.finditer('AG', sequence)]
    if not sub_index: #if substring doesn't exist
      return (sequence, None, mutation)
    pos = random.choice(sub_index)
    new_seq = sequence[:pos] + 'T' + sequence[pos:] 
  elif mutation == 'I': #Insert
    new_seq = sequence[:pos] + different('x') + sequence[pos:]

  elif mutation == 'D': #Deletion
    new_seq = sequence[:pos] + sequence[pos+1:]

  elif mutation == 'U': #Duplication
    new_seq = sequence[:pos] + sequence[pos:pos+n] + sequence[pos:] 
  elif mutation == 'R': #Repeat expansion
    new_seq = sequence[:pos] + sequence[pos:pos+n] * n + sequence[pos:]

  return (new_seq, pos, mutation)