# Numerikus módszerek egyszerűen Python nyelven
# Periodikus függvények közelítése
################################################
from NPY import *

# Tesztadatok beolvasása.
#Az állomány a letölthető programok és adatok között található
(Felirat,M,N,Adat) = mdLoad("Regr_Tesztadatok_TRIG.txt")

# Parametrikus trigonometrikus polinom adatainak kiválasztása
# A függetlenváltozó a betöltött adatmátrix 0. oszlopában,
# a függőválltozó a 2. oszlopában található
(x,y) = mdCol(Adat,2,[0])

# A nyers mérési adatok felrajzolása
R1 = Axes((1024,768),("Periodikus összefüggés ","Periodikus összefüggés vizsgálata"),(0,5*pi),(-8,12),(0,0),(pi/2,2),("3.0f","4.0f"))
dPlot(R1,x,y,"dot","blue")

# Adatok közelítése parametrikus trigonometrikus polinommal
p3 = regrModell("ptrig",(x,y),(3,2,4.31),(4.31,4.315,0.0001))
p3.Print("Periodikus összefüggés közelítése parametrikus trigonometrikus polinommal")

# A közelített együtthatókkal a függvényértékszámítása
x1 = setList(0,5*pi,pi/100)
y1 = DIM(len(x1))
for i in range(len(x1)):
    y1[i] = FNYptrig(p3.Coeff,x1[i],p3.param[0:4])

# A közelített függvényértékek felrajzolása    
dPlot(R1,x1,y1,"line","red")

# A harmonikusok számítása és rajzolása
a = p3.param[3] 
y2 = DIM(len(x1))
# Szinuszos tagok rajzolása
for k in range(1,4):
    for i in range(len(x1)):
        y2[i] = p3.Coeff[k]*sin(k*a*x1[i])
    dPlot(R1,x1,y2,"line","magenta")
# Koszinuszos tagok rajzolása
for k in range(1,3):
    for i in range(len(x1)):
        y2[i] = p3.Coeff[3+k]*cos(k*a*x1[i])
    dPlot(R1,x1,y2,"line","blue")

# Ábra kimentése postscript formátumban
f = "PeriodikusTeszt_abra_V1"
exportPlot(R1,f)

