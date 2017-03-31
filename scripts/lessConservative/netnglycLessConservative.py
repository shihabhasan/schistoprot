import sys
import os
import subprocess


def netnglyc(fileName):
    netNglyc="/home/shihab/tools/netNglyc-1.0/netNglyc"

    n_count=0
    
    command=netNglyc+" "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for line in process.stdout:
        line=line.strip()
        if line!="":
            if line[-1]=="+":
                n_count=n_count+1

    return str(n_count)

    


