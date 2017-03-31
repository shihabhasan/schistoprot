import sys
import os
import subprocess

def charge(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    charge = lines[3].strip().split("=")[-1].replace(" ", "")
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return charge

def molarExtinctionCoefficient(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    ext_coeff =lines[5].strip().split("=")[1].split("(reduced)")[0].replace(" ","")
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return ext_coeff

def absobance(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    absorb = lines[6].strip().split("=")[1].split("(reduced)")[0].replace(" ","")
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return absorb

def probabilityOfExpression(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    inclusion=lines[7].strip().split("=")[1].replace(" ","")
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return inclusion

def alanineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[10].strip().split("\t")[-1]

def cysteineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[12].strip().split("\t")[-1]

def asparticAcidDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[13].strip().split("\t")[-1]

def glutamicAcidDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[14].strip().split("\t")[-1]

def phenylalanineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[15].strip().split("\t")[-1]

def glycineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[16].strip().split("\t")[-1]

def histidineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[17].strip().split("\t")[-1]

def isoleucineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[18].strip().split("\t")[-1]

def lysineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[20].strip().split("\t")[-1]

def leucineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[21].strip().split("\t")[-1]

def methionineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[22].strip().split("\t")[-1]

def asparagineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[23].strip().split("\t")[-1]

def prolineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[25].strip().split("\t")[-1]

def glutamineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[26].strip().split("\t")[-1]


def arginineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[27].strip().split("\t")[-1]

def serineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[28].strip().split("\t")[-1]

def threonineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[29].strip().split("\t")[-1]

def valineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[31].strip().split("\t")[-1]

def tryptophanDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[32].strip().split("\t")[-1]

def tyrosineDayhoffStat(fileName):
    command="pepstats -sequence "+fileName+" -outfile "+"pepstat_"+fileName+" -auto"
    return_code = subprocess.call(command, shell=(sys.platform!="Linux"))
    pepsOut=open("pepstat_"+fileName, "r")
    lines = pepsOut.readlines()
    pepsOut.close()
    os.remove("pepstat_"+fileName)
    return lines[34].strip().split("\t")[-1]


                   
    
    
