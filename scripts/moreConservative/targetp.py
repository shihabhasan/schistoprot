import sys, subprocess, re

def mTP(fileName):
    targetp="/home/shihab/tools/targetp-1.1/targetp"
    command=targetp+" -N "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    lines = process.stdout.readlines()
    predict=re.findall("\d+\.\d+", lines[-3].strip())
    if predict==[]:
        mTP = "0"
    else:
        mTP = predict[-3]
    return mTP

def sP(fileName):
    targetp="/home/shihab/tools/targetp-1.1/targetp"
    command=targetp+" -N "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    lines = process.stdout.readlines()
    predict=re.findall("\d+\.\d+", lines[-3].strip())
    if predict==[]:
        SP = "0"
    else:
        SP = predict[-2]
    return SP

def otherLocation(fileName):
    targetp="/home/shihab/tools/targetp-1.1/targetp"
    command=targetp+" -N "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    lines = process.stdout.readlines()
    predict=re.findall("\d+\.\d+", lines[-3].strip())
    if predict==[]:
        other = "0"
    else:
        other = predict[-1]
    return other


