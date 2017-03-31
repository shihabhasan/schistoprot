import sys
import os
import subprocess


def netphos(fileName):
    netPhos="/home/shihab/tools/ape-1.0/netphos"

    s_count=0
    t_count=0
    y_count=0
    
    command=netPhos+" -2 "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for line in process.stdout:
        line=line.strip()
        if line[0:2]=="%1":
            s=line.count("S")
            t=line.count("T")
            y=line.count("Y")
            s_count=s_count+s
            t_count=t_count+t
            y_count=y_count+y

    return str(s_count)+","+str(t_count)+","+str(y_count)

    


