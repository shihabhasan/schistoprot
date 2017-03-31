from Bio import SeqIO
from Bio.SeqUtils import ProtParam

def seqLength(filename):
    record = SeqIO.read(filename, "fasta")
    return str(len(record.seq))

def molecularWeight(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(X.molecular_weight())

def averageResidueWeight(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(round(X.molecular_weight()/len(record.seq),4))

def alanineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("A"))

def cysteineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("C"))

def asparticAcidCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("D"))

def glutamicAcidCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("E"))

def phenylalanineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("F"))

def glycineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("G"))

def histidineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("H"))

def isoleucineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("I"))

def lysineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("K"))

def leucineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("L"))

def methionineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("M"))

def asparagineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("N"))

def prolineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("P"))

def glutamineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("Q"))

def arginineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("R"))

def serineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("S"))

def threonineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("T"))

def valineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("V"))

def tryptophanCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("W"))

def tyrosineCount(filename):
    record = SeqIO.read(filename, "fasta")
    return str(record.seq.count("Y"))

def tinyMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    return str(count["A"]+count["C"]+count["G"]+count["S"]+count["T"])

def smallMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    return str(count["A"]+count["C"]+count["D"]+count["G"]+count["N"]+count["P"]+count["S"]+count["T"]+count["V"])

def alaninePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("A"))*100/len(record.seq), 4))

def cysteinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("C"))*100/len(record.seq), 4))

def asparticAcidPercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("D"))*100/len(record.seq), 4))

def glutamicAcidPercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("E"))*100/len(record.seq), 4))

def phenylalaninePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("F"))*100/len(record.seq), 4))

def glycinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("G"))*100/len(record.seq), 4))

def histidinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("H"))*100/len(record.seq), 4))

def isoleucinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("I"))*100/len(record.seq), 4))

def lysinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("K"))*100/len(record.seq), 4))

def leucinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("L"))*100/len(record.seq), 4))

def methioninePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("M"))*100/len(record.seq), 4))

def asparaginePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("N"))*100/len(record.seq), 4))

def prolinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("P"))*100/len(record.seq), 4))

def glutaminePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("Q"))*100/len(record.seq), 4))

def argininePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("R"))*100/len(record.seq), 4))

def serinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("S"))*100/len(record.seq), 4))

def threoninePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("T"))*100/len(record.seq), 4))

def valinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("V"))*100/len(record.seq), 4))

def tryptophanPercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("W"))*100/len(record.seq), 4))

def tyrosinePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    return str(round(float(record.seq.count("Y"))*100/len(record.seq), 4))

def tinyMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    tiny = count["A"]+count["C"]+count["G"]+count["S"]+count["T"]
    return str(round(float(tiny)*100/len(record.seq), 4))

def smallMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    small = count["A"]+count["C"]+count["D"]+count["G"]+count["N"]+count["P"]+count["S"]+count["T"]+count["V"]
    return str(round(float(small)*100/len(record.seq), 4))

def aromaticity(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(X.aromaticity())
    
def instabilityIndex(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(X.instability_index())
    
def isoelectricPoint(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(X.isoelectric_point())
    
def gravy(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(X.gravy())

def aliphaticMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    aliphatic = count["I"]+count["L"]+count["V"]
    return str(aliphatic)

def aromaticMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    aromatic = count["F"]+count["H"]+count["W"]+count["Y"]
    return str(aromatic)

def polarMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    polar = count["D"]+count["E"]+count["H"]+count["K"]+count["N"]+count["Q"]+count["R"]+count["S"]+count["T"]
    return str(polar)

def nonPolarMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    nonPolar = count["A"]+count["C"]+count["F"]+count["G"]+count["I"]+count["L"]+count["M"]+count["P"]+count["V"]+count["W"]+count["Y"]
    return str(nonPolar)

def chargedMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    charged = count["D"]+count["E"]+count["H"]+count["K"]+count["R"]
    return str(charged)
    
def acidicMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    acidic = count["D"]+count["E"]
    return str(acidic)
    
def basicMoleCount(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    basic = count["H"]+count["K"]+count["R"]
    return str(basic)

def aliphaticMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    aliphatic = count["I"]+count["L"]+count["V"]
    return str(round(float(aliphatic)*100/len(record.seq), 4))

def aromaticMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    aromatic = count["F"]+count["H"]+count["W"]+count["Y"]
    return str(round(float(aromatic)*100/len(record.seq), 4))

def polarMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    polar = count["D"]+count["E"]+count["H"]+count["K"]+count["N"]+count["Q"]+count["R"]+count["S"]+count["T"]
    return str(round(float(polar)*100/len(record.seq), 4))

def nonPolarMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    nonPolar = count["A"]+count["C"]+count["F"]+count["G"]+count["I"]+count["L"]+count["M"]+count["P"]+count["V"]+count["W"]+count["Y"]
    return str(round(float(nonPolar)*100/len(record.seq), 4))

def chargedMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    charged = count["D"]+count["E"]+count["H"]+count["K"]+count["R"]
    return str(round(float(charged)*100/len(record.seq), 4))
    
def acidicMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    acidic = count["D"]+count["E"]
    return str(round(float(acidic)*100/len(record.seq), 4))
    
def basicMolePercentage(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    count=X.count_amino_acids()
    basic = count["H"]+count["K"]+count["R"]
    return str(round(float(basic)*100/len(record.seq), 4))

def helixFraction(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(round(X.secondary_structure_fraction()[0], 4))

def turnFraction(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(round(X.secondary_structure_fraction()[1], 4))

def sheetFraction(filename):
    record = SeqIO.read(filename, "fasta")
    X = ProtParam.ProteinAnalysis(str(record.seq))
    return str(round(X.secondary_structure_fraction()[2], 4))




      
 



