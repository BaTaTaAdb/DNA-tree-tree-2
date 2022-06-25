'''
Enunciado: https://cs50.harvard.edu/x/2020/psets/6/dna/
'''

def dna_repeating_element(dna,element):
	if element in dna:
		dna_split = dna.split(element)
		consecutive_max = 0
		consecutive = 1
		for i in range(len(dna_split)-1):
			if dna_split[i] == dna_split[i+1] == "" or dna_split[i+1] == "":
				consecutive += 1
			else:
				if consecutive > consecutive_max:
					consecutive_max = consecutive

		return consecutive_max
	else:
		return 0


with open("sequences/1.txt","r") as texto:
	dna = texto.readline()

print(dna_repeating_element(dna,"AGATC"))