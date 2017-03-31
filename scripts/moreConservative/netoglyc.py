import sys
import os
import subprocess


def netoglyc(fileName):
    netOglyc="~/tools/netOglyc-3.1d/netOglyc"

    t_count=0
    
    command=netOglyc+" "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for line in process.stdout:
        line=line.strip()
        if line!="":
            if line[-1]=="-" and "T" in line[-6:]:
                t_count=t_count+1

    return str(t_count)

    


