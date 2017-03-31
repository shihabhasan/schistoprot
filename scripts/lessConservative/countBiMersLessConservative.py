def countBiMers(sequence):
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
    dimerPara=""
    for a1 in amino:
        for a2 in amino:
            dimerPara=dimerPara+","+str(round(bimerDic[(a1+a2)], 4))
    return dimerPara



