from Bio import SeqIO
 
def duplicate_seq_remover(filename):
    outFile=open(filename+"_nodups", "w")
    idList=[]
    records=SeqIO.parse(filename, "fasta")
    for rec in records:
        if rec.id not in idList:
            idList.append(rec.id)
            outFile.write(">"+rec.description+"\n"+str(rec.seq)+"\n")
    outFile.close()

