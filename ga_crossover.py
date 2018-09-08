# Kunal Deshmukh + Eric Tjon
import random

def complement_of(char):
    if char == 'A':
        return 'T'
    elif char == 'T':
        return 'A'
    elif char == 'C':
        return 'G'
    elif char == 'G':
        return 'C'

def crossover(dna):
    dna_complement = []
    dna = list(dna)
    for ele in dna:
        dna_complement.append(complement_of(ele))
    dna_complement = ''.join(dna_complement)
    pos = random.randint(1,len(dna)-1)
    cross_len = random.randint(0,len(dna)-pos)
    print(pos)
    print(cross_len)
    curr_pos = pos 
    for i in range(cross_len):
        dna[curr_pos] = dna_complement[curr_pos]
        curr_pos += 1
    dna = ''.join(dna)
    print (dna,pos+1,cross_len)
    return(dna,pos+1,cross_len)
