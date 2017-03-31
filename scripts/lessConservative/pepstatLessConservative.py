import sys
import os
import subprocess



def pepstat(fileName):
    
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))

    pepsOut=open("pepstat_"+fileName, "r")

    lines = pepsOut.readlines()
    charge = lines[3].strip().split("=")[-1].replace(" ", "")

    ext_coeff =lines[5].strip().split("=")[1].split("(reduced)")[0].replace(" ","")

    absorb = lines[6].strip().split("=")[1].split("(reduced)")[0].replace(" ","")

    inclusion=lines[7].strip().split("=")[1].replace(" ","")

    os.remove("pepstat_"+fileName)

    return (charge+","+ext_coeff+","+absorb+","+inclusion+","+lines[10].strip().split("\t")[-1]+","+lines[12].strip().split("\t")[-1]+","+lines[13].strip().split("\t")[-1]\
                   +","+lines[14].strip().split("\t")[-1]+","+lines[15].strip().split("\t")[-1]+","+lines[16].strip().split("\t")[-1]\
                   +","+lines[17].strip().split("\t")[-1]+","+lines[18].strip().split("\t")[-1]\
                   +","+lines[20].strip().split("\t")[-1]+","+lines[21].strip().split("\t")[-1]+","+lines[22].strip().split("\t")[-1]\
                   +","+lines[23].strip().split("\t")[-1]+","+lines[25].strip().split("\t")[-1]\
                   +","+lines[26].strip().split("\t")[-1]+","+lines[27].strip().split("\t")[-1]+","+lines[28].strip().split("\t")[-1]\
                   +","+lines[29].strip().split("\t")[-1]+","+lines[31].strip().split("\t")[-1]\
                   +","+lines[32].strip().split("\t")[-1]+","+lines[34].strip().split("\t")[-1])
                   
    
    
