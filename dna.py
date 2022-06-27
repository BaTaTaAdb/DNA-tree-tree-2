'''
Enunciado: https://cs50.harvard.edu/x/2020/psets/6/dna/
'''
from os import listdir
from os.path import isfile, join
import csv
import sys
args = sys.argv


def check_args():
    try:
        with open(args[1], newline='') as database:
            pass
        with open(args[2], "r") as texto:
            pass
    except:
        #print("ERROR: Invalid arguments values.\n")
        print("Usage: python3 dna.py <data.csv> <sequence.txt>")
        exit()


def findmax(adn, STR):
    inicio = 0
    fim = len(STR)
    maximo = 0
    for x in range(len(adn)):
        if adn[inicio:fim] == STR:
            current = 0
            while adn[inicio:fim] == STR:
                current += 1
                inicio += len(STR)
                fim += len(STR)
                maximo = max(current, maximo)
        else:
            inicio += 1
            fim += 1
    return maximo


databases = [f for f in listdir("./databases/")
             if isfile(join("./databases/", f))]
sequences = [f for f in listdir("./sequences/")
             if isfile(join("./sequences/", f))]
#print(databases, sequences)
"""if len(args) < 2:
    print("ERROR: Invalid arguments count.\nUsage: python3 dna.py <data.csv> <sequence.txt>")
    exit()

if check_args():
    print("ERROR: Invalid arguments values.\nUsage: python3 dna.py <data.csv> <sequence.txt>")
    exit()"""

check_args()
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
    repeated = findmax(dna, element)
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
