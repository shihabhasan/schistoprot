from Bio import SeqIO
from Bio.SeqUtils import ProtParam

import sys, os, subprocess
import re
import time, hashlib

from pepstat import pepstat
from garnier import garnier
from netcglyc import netcglyc
from netchop import netchop
from netnglyc import netnglyc
from netphos import netphos
from prop import prop
from anchor import anchor
from targetp import targetp
from bepipred import bepipred
from tmhmm import tmhmm
from signalp import signalp
from immuno import immuno


def features(seqID, sequence):
    parameters=""
         
    seq=sequence.upper().replace("X","").replace("*","").replace("U","C").replace("B","D")

    X = ProtParam.ProteinAnalysis(seq)
    
    count=X.count_amino_acids()
    parameters=parameters+str(len(sequence))+","
    
    percent=X.get_amino_acids_percent()
    parameters=parameters+str(percent["A"])+","+str(percent["C"])+","+str(percent["D"])+","+str(percent["E"])+","+str(percent["F"])\
                   +","+str(percent["G"])+","+str(percent["H"])+","+str(percent["I"])+","+str(percent["K"])+","+str(percent["L"])+","+str(percent["M"])\
                   +","+str(percent["N"])+","+str(percent["P"])+","+str(percent["Q"])+","+str(percent["R"])+","+str(percent["S"])+","+str(percent["T"])\
                   +","+str(percent["V"])+","+str(percent["W"])+","+str(percent["Y"])+","

    

    parameters=parameters+str(X.molecular_weight())+","
    parameters=parameters+str(X.aromaticity())+","
    parameters=parameters+str(X.instability_index())+","
    parameters=parameters+str(X.isoelectric_point())+","
    parameters=parameters+str(X.gravy())+","
    parameters=parameters+str(X.secondary_structure_fraction()[0])+","+str(X.secondary_structure_fraction()[1])+","+str(X.secondary_structure_fraction()[2])+","
    parameters=parameters+str(round(X.molecular_weight()/len(seq),4))+","

    #-----------------------ELEMENTAL COST--------------------------
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

    C=0
    N=0
    S=0
    O=0
    H=0
    X=0
    
    length=len(sequence)
    for amino in seq: 
        C=C+elemDict[amino]['C']
        N=N+elemDict[amino]['N']
        S=S+elemDict[amino]['S']
        O=O+elemDict[amino]['O']
        H=H+elemDict[amino]['H']
    Ccost=str(round(float(C)/length,4))
    Ncost=str(round(float(N)/length,4))
    Scost=str(round(float(S)/length,4))
    Ocost=str(round(float(O)/length,4))
    Hcost=str(round(float(H)/length,4))
    parameters=parameters+Ccost+","+Ncost+","+Scost+","+Ocost+","+Hcost+","


    #-----------------------PEPSTATS-------------------------------
    
    inFileName=seqID.replace("|","_").replace(":","_")+"_"+hashlib.md5(time.asctime()).hexdigest()
    inFasta=open(inFileName, "w")
    inFasta.write(">"+seqID.replace("|","_")+"\n"+seq+"\n")
    inFasta.close()

    parameters=parameters+pepstat(inFileName)+","
                   

    tiny = count["A"]+count["C"]+count["G"]+count["S"]+count["T"]
    tiny_per = round(((float(tiny)/len(seq))*100),3)
    parameters=parameters+str(tiny_per)+","

    small = count["A"]+count["C"]+count["D"]+count["G"]+count["N"]+count["P"]+count["S"]+count["T"]+count["V"]
    small_per = round(((float(small)/len(seq))*100),3)
    parameters=parameters+str(small_per)+","

    aliphatic = count["I"]+count["L"]+count["V"]
    aliphatic_per = round(((float(aliphatic)/len(seq))*100),3)
    parameters=parameters+str(aliphatic_per)+","

    aromatic = count["F"]+count["H"]+count["W"]+count["Y"]
    aromatic_per = round(((float(aromatic)/len(seq))*100),3)
    parameters=parameters+str(aromatic_per)+","

    polar = count["D"]+count["E"]+count["H"]+count["K"]+count["N"]+count["Q"]+count["R"]+count["S"]+count["T"]
    polar_per = round(((float(polar)/len(seq))*100),3)
    parameters=parameters+str(polar_per)+","

    nonPolar = count["A"]+count["C"]+count["F"]+count["G"]+count["I"]+count["L"]+count["M"]+count["P"]+count["V"]+count["W"]+count["Y"]
    nonPolar_per = round(((float(nonPolar)/len(seq))*100),3)
    parameters=parameters+str(nonPolar_per)+","

    charged = count["D"]+count["E"]+count["H"]+count["K"]+count["R"]
    charged_per = round(((float(charged)/len(seq))*100),3)
    parameters=parameters+str(charged_per)+","
    
    acidic = count["D"]+count["E"]
    acidic_per = round(((float(acidic)/len(seq))*100),3)
    parameters=parameters+str(acidic_per)+","
    
    basic = count["H"]+count["K"]+count["R"]
    basic_per = round(((float(basic)/len(seq))*100),3)
    parameters=parameters+str(basic_per)+","
    


    #------------------------GARNIER--------------------------------

    parameters=parameters+garnier(inFileName)+","


    #--------------------------NetCGlyc--------------------------------

    parameters=parameters+netcglyc(inFileName)+","

    #--------------------------NetChop--------------------------------

    parameters=parameters+netchop(inFileName)+","
    

    #--------------------------NetNGlyc--------------------------------

    parameters=parameters+netnglyc(inFileName)+","
    

    #--------------------------NetPhos--------------------------------

    parameters=parameters+netphos(inFileName)+","


    #--------------------------ProP----------------------------------

    parameters=parameters+prop(inFileName)+","


    #--------------------------ANCHOR----------------------------------

    parameters=parameters+anchor(inFileName)+","

    #--------------------------TargetP----------------------------------

    parameters=parameters+targetp(inFileName)+","

    #--------------------------BepiPred----------------------------------

    parameters=parameters+bepipred(inFileName)+","


    #--------------------------TMHMM----------------------------------

    parameters=parameters+tmhmm(inFileName)+","


    #--------------------------Immunogenicity----------------------------------

    parameters=parameters+immuno(inFileName)

    #--------------------------#####################---------------------


    os.remove(inFileName)
    
    return parameters

    
