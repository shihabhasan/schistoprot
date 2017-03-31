import sys, subprocess, re

def targetp(fileName):
    targetp="/home/shihab/tools/targetp-1.1/targetp"

    command=targetp+" -N "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()

    predict=re.findall("\d+\.\d+", lines[-3].strip())
    if predict==[]:
        mTP = "0"
        SP = "0"
        other = "0"
    else:
        mTP = predict[-3]
        SP = predict[-2]
        other = predict[-1]

    return (mTP+","+SP+","+other)

