# Numerikus módszerek egyszerűen Python nyelven
# Közönséges differenciálegyenletrendszerek 
# megoldási módszereinek összehasonlítása
################################################

from NPY import *

# A differenciálegyenlet rendszert leíró függvény
def fn(t,y):
    "A kör differenciálegyenletként felírva"
    # Kör egyenlete
    Y = DIM(2)
    Y[0] = -y[1]
    Y[1] = y[0]
    return(Y)

# Az fn-ben leírt differenciálegyenlet analitikus (pontos) megoldása (ha ismert)
def fnp(t):
    "Pontos megoldás"
    pY = DIM(2)
    pY[0] = cos(t)
    pY[1] = sin(t)
    return(pY)

# A megoldáshoz használt paraméterek
a = 0
b = 2*pi
n = 26

# Kezdeti értékek
Y0 = DIM(2)
Y0[0] = 1
Y0[1] = 0

# Runge-Kutta közelítés
[h,t,yRK4] = diffERungeKutta(fn,Y0,a,b,n,"RK4")
# Pontos érték
yP = DIM(2,len(t))
for i in range(len(t)):
    y = fnp(t[i])
    yP[0][i] = y[0]
    yP[1][i] = y[1]

# Milne-Hamming prediktor-korrektor módszer
[h,t,yMH] = diffEMilneHamming(fn,Y0,a,b,n)
print("Differenciálegyenletrendszer megoldási módszereinek összehasonlítása")
print("h:",h)
print("        t        pontos y(0)    pontos y(1)   RK4 y(0)     RK4 y(1)     MH y(0)      MH y(1)")
Y1 = mConcat(t,matrTrans(yP))
Y1 = mConcat(Y1,matrTrans(yRK4))
Y1 = mConcat(Y1,matrTrans(yMH))
mPrint(Y1,"13.4f")
print("\n")

# Eredmények grafikus megjelenítése
s1 = "Közönséges differenciálegyenlet rendszerek megoldási módszereinek összehasonlítása"
s2 = "Közönséges differenciálegyenlet rendszerek \n megoldási módszereinek összehasonlítása"
rajz = Axes((1024,768),(s1,s2),(-1,1),(-1,1),(0,0),(0.2,.2),("3.1f","3.1f"))
dPlot(rajz,mdCol(Y1,1),mdCol(Y1,2),'line','blue')
dPlot(rajz,mdCol(Y1,3),mdCol(Y1,4),'line','red')
dPlot(rajz,mdCol(Y1,5),mdCol(Y1,6),'line','green')
exportPlot(rajz,"Kor_differencialegyenlete")
