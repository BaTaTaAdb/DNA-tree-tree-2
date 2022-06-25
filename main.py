'''
Enunciado: https://cs50.harvard.edu/x/2020/psets/6/dna/
'''
with open("sequences/11.txt","r") as texto:
	dna = texto.readline()
dna_split_AGATC = dna.split("AGATC")
for i in dna_split_AGATC