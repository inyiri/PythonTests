# Numerikus módszerek egyszerűen Python nyelven
# Interpolációs eljárások bemutatása lépcsősfüggvényen
######################################################         

from NPY import *


# Lépcsősfüggvény létrehozása
X = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Y = [-1,-1,-1,-1,-1,1,1,1,1,1,-1,-1,-1,-1,-1]
nX = len(X)
x = setList(3,15,0.05)
n = len(x)
N = 2
yl = DIM(n)
yn = DIM(n)
ya = DIM(n)

# Lagrange interpoláció
for i in range(n):
    yl[i] = interpolLagrange(x[i],N,X,Y)

# Newton interpoláció
for i in range(n):
    yn[i] = interpolNewton(x[i],2,X,Y)

# Akima spline interpoláció
for i in range(n):
    ya[i] =  interpolAkima(x[i],X,Y)

# Összesített rajz
Felirat = "A Lagrange,Newton és Akima féle spline interpolációs eljárások bemutatása\n lépcsős függvény esetén"
rajz = Axes((1024,768),("Interpoláció",Felirat),(0,16),(-2,2),(0,0),(1,0.5),("3.1f","3.1f"))
dPlot(rajz,X,Y)
dPlot(rajz,x,yl,"line","Blue")
dPlot(rajz,x,yn,"line","Green")
dPlot(rajz,x,ya,"line","Black")

# Rajz exportálása
exportPlot(rajz,"Interpolaciosteszt_Eredmeny")
