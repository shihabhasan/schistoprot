import sys, subprocess


def bepipred(fileName):
    bepipred="/home/shihab/tools/bepipred-1.0b/bepipred"
    w_count=0
    
    command=bepipred+" "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for line in process.stdout:
        line=line.strip()
        if line[-2:]==" E":
            w_count=w_count+1

    return str(w_count)

    


