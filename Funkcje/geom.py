#do lekcji 52

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #ciąg geometryczny
    value = a1*pow(factor,index-1)
    return value

def GiveFactorForGeomSeq(term, nextterm):
    #dwa elementy
    return nextterm/term

def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    #suma elementów ciągu
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN