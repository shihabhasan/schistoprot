import subprocess


def genericPhosphorylationSerine(fileName):
    s_count=0
    netPhos="~/tools/ape-1.0/netphos"
    command=netPhos+" -2 "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    for line in process.stdout:
        line=line.strip()
        if line[0:2]=="%1":
            s=line.count("S")
            s_count=s_count+s
    return str(s_count)

    
def genericPhosphorylationThreonine(fileName):
    t_count=0
    netPhos="~/tools/ape-1.0/netphos"
    command=netPhos+" -2 "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    for line in process.stdout:
        line=line.strip()
        if line[0:2]=="%1":
            t=line.count("T")
            t_count=t_count+t
    return str(t_count)


def genericPhosphorylationTyrosine(fileName):
    y_count=0
    netPhos="~/tools/ape-1.0/netphos"
    command=netPhos+" -2 "+fileName
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    for line in process.stdout:
        line=line.strip()
        if line[0:2]=="%1":
            y=line.count("Y")
            y_count=y_count+y
    return str(y_count)



    


