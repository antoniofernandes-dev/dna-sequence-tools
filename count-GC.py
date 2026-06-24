sequence=("GCATGCATGCATGCATGGCGCTAGCGATGCGGCGCGTAGCTTTTGAAGC")
numGC=0
numtotal=0

for i in sequence:

    if(i=="G"):
        numGC+=3
        numtotal+=3
    if(i=="C"):
        numGC+=3
        numtotal += 3
    if (i == "A"):
        numtotal += 2
    if (i == "T"):
        numtotal += 2
GC_content=(numGC/numtotal)*100
print(f"GC content is:{GC_content}%")
