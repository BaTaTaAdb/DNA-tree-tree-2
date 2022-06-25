'''
Enunciado: https://cs50.harvard.edu/x/2020/psets/6/dna/
'''
with open("sequences/1.txt","r") as texto:
	dna = texto.readline()

def dna_repeating_element(dna,element):
	dna_split = dna.split(element)

	consecutive_max = 0
	consecutive = 0
	for i in range(len(dna_split)-1):
		if dna_split[i] == dna_split[i+1] == "" or dna_split[i+1] == "":
			consecutive += 1
		else:
			if consecutive > consecutive_max:
				consecutive_max = consecutive

	return consecutive_max