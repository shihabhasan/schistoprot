import sys
import os
import subprocess
import re


def netchop(fileName):
    netChop="/home/shihab/tools/netchop-3.1/bin/netChop"

    command="export NETCHOP=/home/shihab/tools/netchop-3.1; export TMPDIR=/home/shihab/tools/netchop-3.1/tmp; "+netChop+" -s "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()

    predict=re.findall("\d+", lines[-3].strip())[0]

    return predict

    

