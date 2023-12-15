import itertools
#from save_func import *
from hamilton_bruteforce import *

# Inputs: series of strings in format fasta
# Output: completed string in format fasta made from readings

#Inputs: 
path = r"C:\Users\user\Desktop\Coding\bioinf\example_readings.fa"
file = open(path)
readings = (file.read().split('\n'))
head = readings.pop(0)
file.close()

# we put into program N readings with length = k  
len_readings = len(readings[0])
number_of_readings = len(readings)
print(readings, len_readings, number_of_readings)

pre = [readings[0][0:len_readings-1]]
suf = [readings[0][1:]]
nodes = []
links = []
#de Bruijn graph making
for i in range(1, number_of_readings): 
    pre.append(readings[i][0:len_readings-1])
    suf.append(readings[i][1:])
    for j in range(len(pre)): 
        if pre[i] == suf[j] and i != j :
            #print(pre[i])
            nodes.append(pre[i])
            links.append((j, i))
        if suf[i] == pre[j] and i!= j:
            #print(pre[j])
            nodes.append(pre[j])
            links.append((i,j))

#print(pre, suf)
#print(nodes, links, len(nodes), len(links))

#finding Hamiltonian path 
work_nodes = list(range(len(nodes)))
order = hamilton_bruteforce(work_nodes, links)

#assembling 
genome = readings[order[0]]
for i in range(1, len(order)):
    genome += readings[order[i]][-1]

print(genome)


