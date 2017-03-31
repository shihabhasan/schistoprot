import sys
import os
import subprocess
import re


def secondaryHelixCount(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_count = re.findall("\d+", lines[-11].strip())
    if sec_str_count ==[]:
        sec_helix_count = "0"
    else:
        sec_helix_count = sec_str_count[0]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_helix_count

def secondarySheetCount(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_count = re.findall("\d+", lines[-11].strip())
    if sec_str_count ==[]:
        sec_sheet_count = "0"
    else:
        sec_sheet_count = sec_str_count[1]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_sheet_count

def secondaryTurnsCount(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_count = re.findall("\d+", lines[-11].strip())
    if sec_str_count ==[]:
        sec_turns_count = "0"
    else:
        sec_turns_count = sec_str_count[2]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_turns_count

def secondaryCoilCount(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_count = re.findall("\d+", lines[-11].strip())
    if sec_str_count ==[]:
        sec_coil_count = "0"
    else:
        sec_coil_count = sec_str_count[3]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_coil_count

def secondaryHelixPercentage(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_percent = re.findall("\d+", lines[-10].strip())
    if sec_str_percent ==[]:
        sec_helix_percent = "0"
    else:
        sec_helix_percent = sec_str_percent[0]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_helix_percent

def secondarySheetPercentage(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_percent = re.findall("\d+", lines[-10].strip())
    if sec_str_percent ==[]:
        sec_sheet_percent = "0"
    else:
        sec_sheet_percent = sec_str_percent[1]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_sheet_percent

def secondaryTurnsPercentage(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_percent = re.findall("\d+", lines[-10].strip())
    if sec_str_percent ==[]:
        sec_turns_percent = "0"
    else:
        sec_turns_percent = sec_str_percent[2]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_turns_percent

def secondaryCoilPercentage(fileName):
    command="garnier -sequence "+fileName+" -outfile "+"garnier_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    garnierOut=open("garnier_"+fileName, "r")
    lines = garnierOut.readlines()
    sec_str_percent = re.findall("\d+", lines[-10].strip())
    if sec_str_percent ==[]:
        sec_coil_percent = "0"
    else:
        sec_coil_percent = sec_str_percent[3]
    garnierOut.close()
    os.remove("garnier_"+fileName)
    return sec_coil_percent    
