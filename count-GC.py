sequence=("GCATGCATGCATGCATGGCGCTAGCGATGCGGCGCGTAGCTTTTGAAGC")
num_total=len(sequence)
numA=0
numC=0
numG=0
numT=0
for nucleotide in sequence:
    if nucleotide=="A":
        numA+=1
    if nucleotide=="C":
        numC+=1
    if nucleotide=="G":
        numG+=1
    if nucleotide=="T":
        numT+=1
gc_perc=((numG+numC)/num_total)*100
print(f'Nucleotide A: {numA}')
print(f'Nucleotide C: {numC}')
print(f'Nucleotide G: {numG}')
print(f'Nucleotide T: {numT}')
print(f'GC: {gc_perc}%')
