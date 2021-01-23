import geom
print('2^64 =',geom.GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=11
for i in range(1,maxindex+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')
print('Factor is', geom.GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')
print('Sum of n elements is', geom.GiveSumOfNElementsGeomSeq(2,3,4))