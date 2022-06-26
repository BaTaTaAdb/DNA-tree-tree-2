'''
Enunciado: https://cs50.harvard.edu/x/2020/psets/6/dna/
'''
from os import listdir
from os.path import isfile, join
import csv
import sys
args = sys.argv


def dna_repeating_element(dna, element):
    if element in dna:
        dna_split = dna.split(element)
        consecutive_max = 0
        consecutive = 1
        # print(dna_split)
        for i in range(len(dna_split)-1):
            if dna_split[i] == dna_split[i+1] == "" or dna_split[i+1] == "":
                consecutive += 1
            else:
                if consecutive > consecutive_max:
                    consecutive_max = consecutive

        return consecutive_max
    else:
        return 0


databases = [f for f in listdir("./databases/")
             if isfile(join("./databases/", f))]
sequences = [f for f in listdir("./sequences/")
             if isfile(join("./sequences/", f))]
#print(databases, sequences)
if len(args) < 2:
    print("ERROR: Invalid arguments count.\nUsage: python3 dna.py <data.csv> <sequence.txt>")
    exit()
"""if not (args[1] in databases and args[2] in sequences):
	print("ERROR: Invalid arguments values.\nUsage: python3 dna.py <data.csv> <sequence.txt>")
	exit()"""

# get database
with open(args[1], newline='') as database:
    reader = csv.reader(database)
    database_list = list(reader)

# get dna from sequence argument
with open(args[2], "r") as texto:
    dna = texto.readline()

dna_elements_list = database_list[0][1::]
person_dna = []
for element in dna_elements_list:
    repeated = dna_repeating_element(dna, element)
    person_dna.append(repeated)
    #print(f"{element}: {repeated}")
# print(person_dna)

for i in database_list[1::]:
    # print(i[1::])
    test_list = [int(j) for j in i[1::]]
    # print(test_list)
    if test_list == person_dna:
        print(i[0])
        exit()
print(person_dna)
print("No match")


# for dna in
# print(dna_repeating_element(dna,"AGATC"))
