import sys
import os
import subprocess
import re




    #------------------------GARNIER--------------------------------
def garnier(fileName):

    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))

    garnierOut=open("garnier_"+fileName, "r")

    lines = garnierOut.readlines()

    sec_str_per = re.findall("\d+.\d+", lines[-10].strip())

    if sec_str_per ==[]:
        sec_helix_per = "0"
        sec_sheet_per = "0"
        sec_turns_per = "0"
        sec_coil_per = "0"
    else:
        sec_helix_per = sec_str_per[0]
        sec_sheet_per = sec_str_per[1]
        sec_turns_per = sec_str_per[2]
        sec_coil_per = sec_str_per[3]

    os.remove("garnier_"+fileName)
    
    return (sec_helix_per+","+sec_sheet_per+","+sec_turns_per+","+sec_coil_per)

    
