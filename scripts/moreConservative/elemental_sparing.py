from Bio import SeqIO

elemDict={'A':{'C':3,'N':1,'S':0,'O':2,'H':7}, 'R':{'C':6,'N':4,'S':0,'O':2,'H':14},
   'N':{'C':4,'N':2,'S':0,'O':3,'H':8}, 'D':{'C':4,'N':1,'S':0,'O':4,'H':7},
   'C':{'C':3,'N':1,'S':1,'O':2,'H':7}, 'E':{'C':5,'N':1,'S':0,'O':4,'H':9},
   'Q':{'C':5,'N':2,'S':0,'O':3,'H':10}, 'G':{'C':2,'N':1,'S':0,'O':2,'H':5},
   'H':{'C':6,'N':3,'S':0,'O':2,'H':9}, 'I':{'C':6,'N':1,'S':0,'O':2,'H':13},
   'L':{'C':6,'N':1,'S':0,'O':2,'H':13}, 'K':{'C':6,'N':2,'S':0,'O':2,'H':14},
   'M':{'C':5,'N':1,'S':1,'O':2,'H':11}, 'F':{'C':9,'N':1,'S':0,'O':2,'H':11},
   'P':{'C':5,'N':1,'S':0,'O':2,'H':9}, 'S':{'C':3,'N':1,'S':0,'O':3,'H':7},
   'T':{'C':4,'N':1,'S':0,'O':3,'H':9}, 'W':{'C':11,'N':2,'S':0,'O':2,'H':12},
   'Y':{'C':9,'N':1,'S':0,'O':3,'H':11}, 'V':{'C':5,'N':1,'S':0,'O':2,'H':11}} 


def carbonCount(filename):
    C=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        C=C+elemDict[amino]['C']
    return str(C)

def nitrogenCount(filename):
    N=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        N=N+elemDict[amino]['N']
    return str(N)

def sulphurCount(filename):
    S=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        S=S+elemDict[amino]['S']
    return str(S)

def oxygenCount(filename):
    O=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        O=O+elemDict[amino]['O']
    return str(O)

def hydrogenCount(filename):
    H=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        H=H+elemDict[amino]['H']
    return str(H)

def carbonSparingAverage(filename):
    C=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        C=C+elemDict[amino]['C']
    return str(round(float(C)/len(record.seq), 4))

def nitrogenSparingAverage(filename):
    N=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        N=N+elemDict[amino]['N']
    return str(round(float(N)/len(record.seq), 4))

def sulphurSparingAverage(filename):
    S=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        S=S+elemDict[amino]['S']
    return str(round(float(S)/len(record.seq), 4))

def oxygenSparingAverage(filename):
    O=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        O=O+elemDict[amino]['O']
    return str(round(float(O)/len(record.seq), 4))

def hydrogenSparingAverage(filename):
    H=0
    record = SeqIO.read(filename, "fasta")
    for amino in str(record.seq):
        H=H+elemDict[amino]['H']
    return str(round(float(H)/len(record.seq), 4))
    
