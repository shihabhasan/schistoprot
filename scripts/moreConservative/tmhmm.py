import sys, subprocess


def transmembraneHelices(fileName):
    tmHmm="/home/shihab/tools/tmhmm-2.0c/bin/tmhmm"

    command=tmHmm+" -short "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    lines = process.stdout.readlines()

    helix_count=lines[0].split("\t")[4].split("=")[-1]

    return helix_count

    


