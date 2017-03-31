import sys
import os
import subprocess


def cMannosylation(fileName):
    netCglyc="/home/shihab/tools/netCglyc-1.0/netCglyc"
    w_count=0
    
    command=netCglyc+" -f old "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for line in process.stdout:
        line=line.strip()
        if line[-1]=="W":
            w_count=w_count+1


    return str(w_count)

    


