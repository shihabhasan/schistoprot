def countBiMers(sequence, bimerList):
    # creating hash
    bimerDic = {} 
    amino = 'ACDEFGHIKLMNPQRSTVWY'
    for a1 in amino:
        for a2 in amino:
            bimerDic[a1+a2] = 0.0

    # creating window
    for i in range(0,len(sequence)-1):
        s = sequence[i:i+2]
        bimerDic[s] +=1.0/float(len(sequence))
        
    # creating bimers parameters
    bimerPara={}
    for a1 in amino:
        for a2 in amino:
            bimerPara[a1+a2]=str(round(bimerDic[(a1+a2)], 4))

    bimerListPara=""
    
    for bimer in bimerList:
        bimerListPara=bimerListPara+bimerPara[bimer]+","
    bimerListPara = bimerListPara.rstrip(",")
    return bimerListPara



