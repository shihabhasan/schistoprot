import sys
import os
import subprocess
import re

def prop(fileName):
    proP="/home/shihab/tools/prop-1.0c/prop"

    command=proP+" "+fileName 

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    prop_count=""

    for line in process.stdout:
        if "Propeptide cleavage sites predicted:" in line:
            prop_count=prop_count+re.findall("\d+", line)[0]


    return prop_count

    


