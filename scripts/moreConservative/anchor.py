import sys, subprocess, re

def bindingRegionsDisordered(fileName):
    anchor="/home/shihab/tools/ANCHOR/anchor"

    command=anchor+" "+fileName+" -d /home/shihab/tools/ANCHOR/"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()
    predictions=[]
    for line in lines:
        if line[0]!="#":
            predict=re.findall("\d+", line.strip())
            predictions.append(predict)
    if predictions==[]:
        anchor_res="0"
    else:
        anchor_res=predictions[0]
    return anchor_res[0]

