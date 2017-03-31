import sys, subprocess

def immuno(fileName):
    immunogenecity="/home/shihab/tools/immunogenicity/predict_immunogenicity.py"

    command=immunogenecity+" "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()
    prediction=str(round(float(lines[-1].strip()), 4))
    return prediction

