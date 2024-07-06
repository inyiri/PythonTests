# Numerikus módszerek egyszerűen Python nyelven
# A mdSmooth és mdFocus függvénypár használatának bemutatása
# Az SV Cam fedési változó háromszín (U,V,B) fotoelektromos mérési
# adatainak felhasználásával


# A nyers mérési adatok beolvassa után először egy heurisztikus simításra
# kerül sor,majd az így kapott adatok interpolációval időben egyenközű
# lépéseket tartalmazó skálára kerülnek áttranszformálásra

from NPY import *

# Az adatfájl beolvasása
(Felirat,N,M,data) = mdReadCSV("SVCamTesztadatok.txt",",")
print(Felirat)

# Adatok kiválasztása és transzformálása
# A 0.,2. és 4. oszlopok az időadatokat tartalmazzák tört napokban
# Az 1.,3. és 5. oszlopok a fényesség adatokat tartalmazzák magnitúdóban
# A fájlban található mérési adatok egész számok!
# A valós magnitúdó értékhez  0.0001-el kell szorozni
# Sárga szűrő 
(timeV,magnV) = mScal(0.0001,mdCol(data,1,[0]))
# Kék szűrő
(timeB,magnB) = mScal(0.0001,mdCol(data,3,[2]))
# UV szűrő
(timeU,magnU) = mScal(0.0001,mdCol(data,5,[4]))

# A natív mérési adatok felrajzolása
# A rajzolás fordítva történik!!! A nagy pozitív értékek alacsony fényességnek
# felelnek meg
Fejlec = str(Felirat)+"\n U-B-V fotoelektromos mérések"
p1 = Axes((1600,900),(Felirat,Fejlec),(0.2,0.6),(-1.6,-0.4),(0.2,-0.4),(0.05,0.2),("4.2f","3.1f"))
dPlot(p1,timeV,mScal(-1,magnV),"dot","Red")
dPlot(p1,timeB,mScal(-1,magnB),"dot","Blue")
dPlot(p1,timeU,mScal(-1,magnU),"dot","Magenta")

# Az adatok simítása
# Sárga szűrő
nf = 9
tol = 4
(newNV,timeNV,magnNV,LostV,errV) = mdSmooth(timeV,magnV,nf,tol)
# Kék szűrő
nf = 7
tol = 5
(newNB,timeNB,magnNB,LostB,errB) = mdSmooth(timeB,magnB,nf,tol)
# Ultraibolya szűrő
nf = 9
tol = 5
(newNU,timeNU,magnNU,LostU,errU) = mdSmooth(timeU,magnU,nf,tol)

# A símitott adatok időben egyenközű felosztásra történő transzformálása
tMin = min((min(timeV),min(timeB),min(timeU)))
tMax = max((max(timeV),max(timeB),max(timeU)))
Time = setList(tMin,tMax,0.0005)
nT = len(Time)
ekvV = DIM(nT)
ekvB = DIM(nT)
ekvU = DIM(nT)
# Sárga szűrő
for i in range(nT):
    ekvV[i] = interpolLagrange(Time[i],2,timeNV,magnNV)
# Kék szűrő
for i in range(nT):
    ekvB[i] = interpolLagrange(Time[i],2,timeNB,magnNB)
# Ultraibolya szűrő
for i in range(nT):
    ekvU[i] = interpolLagrange(Time[i],1,timeNU,magnNU)
    
# Eredmények
print("Sárga szűrő (vizuális)")
print("nf:",nf,"   tol:",tol)
print("Megmaradt mérési pontok száma:",newNV)
print("Kieső mérési pontok:")
mPrint(mdRow(LostV,0,len(LostV)-1))
dPlot(p1,timeNV,mScal(-1,magnNV),"line","Red")
dPlot(p1,Time,mScal(-1,ekvV),"line","Black")
print("Kék szűrő")
print("nf:",nf,"   tol:",tol)
print("Megmaradt mérési pontok száma:",newNB)
print("Kieső mérési pontok:")
mPrint(mdRow(LostB,0,len(LostB)-1))
dPlot(p1,timeNB,mScal(-1,magnNB),"line","Blue")
dPlot(p1,Time,mScal(-1,ekvB),"line","Black")
print("Ultraibolya szűrő")
print("nf:",nf,"   tol:",tol)
print("Megmaradt mérési pontok száma:",newNU)
print("Kieső mérési pontok:")
mPrint(mdRow(LostU,0,len(LostU)-1))
dPlot(p1,timeNU,mScal(-1,magnNU),"line","Magenta")
dPlot(p1,Time,mScal(-1,ekvU),"line","Black")
exportPlot(p1,"SVCam_Ekv_Rajz")

