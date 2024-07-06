# Numerikus módszerek egyszerűen Python nyelven
# Közönséges differenciálegyenlet megoldó módszerek
# összehasonlítása
#########################################################

# A Python math moduljából felhasznált függvények
from NPY import *

# A differenciálegyenletet leíró függvény
def fn(t,y):
    "Megoldandó differenciálegyenlet"
    return(y)

# Az fn-ben leírt differenciálegyenlet analitikus (pontos) megoldása
def fnp(t,q):
    "A megoldandó differenciálegyenlet analitikus (pontos) megoldása"
    q = q[0]
    return(exp(q*t))

# A megoldáshoz szükséges paraméterek
a = 0
b = 1
n = 20
y0 = 1

# A pontos megoldást szolgáltató függvényben van függetlenváltozón
# kívüli paraméter
q = DIM(1)
q[0] = 1

# Második példa differenciálegyenlet
#def fn(t,y):
#    "Differenciálegyenlet"
#    return(cos(t)*y**2)
#def fnp(t):
#    "Pontos megoldás"
#    return(1/(1.4-sin(t)))


# Nyomtatás
# A nyomtatáshoz egyetlen Res nevű mátrixot hozunk létre
pr = "y"

# Javított Euler módszer
[h,t,y1]= diffRungeKutta(fn,y0,a,b,n,method="EUL")
Res = DIM(len(t))

# Pontos megoldás
yp = evalPFunc(t,fnp,[1])
Res = mConcat(t,yp)
Res = mConcat(Res,y1)

# Másodrendű Runge-Kutta
[h,t,y2]= diffRungeKutta(fn,y0,a,b,n,method="RK2")
Res = mConcat(Res,y2)

# Heun 3-ad rendű módszere
[h,t,y3]= diffRungeKutta(fn,y0,a,b,n,method="RK3")
Res = mConcat(Res,y3)

# Kutta 4-ed rendűmódszere
[h,t,y4]= diffRungeKutta(fn,y0,a,b,n)
Res = mConcat(Res,y4)

# AMilne-Hamming prediktor-korrektor módszer
[h,tm,yMH] = diffMilneHamming(fn,y0,a,b,n)
Res = mConcat(Res,mdRow(yMH,0,len(Res)))

# Eredmények nyomtatása
if( pr=="y" ):
    print("Közönséges differenciálegyenletek megoldási módszereinek összehasonlítása")
    print("Runge-Kutta módszerek és Milne-Hamming prediktor-korrektor módszer\n")
    print("         t        pontos        EUL        RK2         RK3          RK4         MH")        
    mPrint(Res)

# Eredmények grafikus megjelenítése
s1 = " Közönséges differenciálegyenletek megoldási módszereinek összehasonlítása"
s2 = "Pontos megoldás, 2-ed redű Runge-Kutta és Milne-Hamming módszer"
rajz = Axes((1024,768),(s1,s2),(0,1),(1,3),(0,1),(0.1,1),("2.1f","3.1f"))
dPlot(rajz,t,yp,'dot','blue')
dPlot(rajz,t,y2,'line','red')
dPlot(rajz,tm,yMH,'line','green')

# Az ábra kimentése
#exportPlot(rajz,"KozonsegesDifferencialegyenletRajz")
