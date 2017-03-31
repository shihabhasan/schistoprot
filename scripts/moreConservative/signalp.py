import sys
import os
import subprocess


def signalPeptides(fileName):
    signalP="/home/shihab/tools/signalp-4.1/signalp"

    t_count=0
    
    command=signalP+" -f summary "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()

    if "SP='YES'" in lines[-1]:
        return "1"
    else:
        return "0"


    


