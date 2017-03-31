from Bio import SeqIO

def seqcount(fileName):
    records=SeqIO.parse(fileName, "fasta")
    count=0
    for record in records:
        count=count+1
    return count
