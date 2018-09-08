# Kunal Deshmukh + Eric Tjon
#Not complete

import random
import ga_crossover
import ga_mutation

file = open('dna_sequences.dat')
lst = [] 
for line in file:
    lst += [line.split()]
result =''
mut_file = open("mutation_results.dat", 'w')
for ele in lst:
    option = random.randint(1, 6)
    if option == 1:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'M') + '\n')
    elif option == 2:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'N') + '\n')
    elif option == 3:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'I') + '\n')
    elif option == 4:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'D') + '\n')
    elif option == 5:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'U') + '\n') # Please check this call
    else:
        mut_file.write(str(ga_mutation.mutate(ele[0]),'R') + '\n') # Please check this call
mut_file.close()

cross_file = open("crossover_results.dat",'w')
for ele in lst:
    cross_file.write(str(ga_crossover.crossover(ele[0]))+'\n')
cross_file.close()