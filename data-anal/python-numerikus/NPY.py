#coding: utf-8

# Numerikus módszerek egyszerűen Python nyelven
# Tekler V.
# A könyvben található valamennyi eljárás
###############################################            

# Külső függvények
from math     import *
from tkinter  import *
from datetime import datetime
#############################

# Deklarációs függvények
########################

def vectNULL(n):
    "n elemű ZÉRÓ vektor létrehozása"
    # A függvény helyett a DIM(n) függvény is használható
    return([0 for i in range(n)])


def matrNULL(n,m):
    "n sorból és m oszlopból álló ZÉRÓ mátrix létrehozása"
    # A függvény helyett a DIM(n,m) függvény is használható
    if( m==1 ):
        #n elemű vektort kell létrehozni
        return([0 for i in range(n)])
    else:
        # n sorból és m oszlopból álló mátrixot kell létrehozni
        return([[0]*m for i in range(n)])


def DIM(n=1,m=1,val=0):
    "Egy- és kétdimenziós tömb létrehozása, adott értékű elemekkel"
    # Ez a függvény a matrNULL és a vectNULL függvények helyett használható
    # Ha n<1 vagy m<1, akkor hibaüzenet jelenik meg és a visszatérési érték 0
    if( m<1 or n<1 ):
        print("Hibás dimenzió!")
        return(0)
    if( m==1 ):
        #n elemű vektort kell létrehozni
        return([val for i in range(n)])
    else:
        # n sorból és m oszlopból álló mátrixot kell létrehozni
        return([[val]*m for i in range(n)])


def COMPLEX(n=1,m=1,val=complex(0,0)):
    "n sorból és m oszlopból álló (0,0j) értékű komplex elemeket tartalmazó mátrix létrehozása"
    # Ha n<1 vagy m<1, akkor hibaüzenet jelenik meg és a visszatérési érték 0
    if( m<1 or n<1 ):
        print("Hibás dimenzió!")
        return(0)
    if( m==1 ):
        #n elemű vektort kell létrehozni
        return([val for i in range(n)])
    else:
        # n sorból és m oszlopból álló mátrixot kell létrehozni
        return([[val]*m for i in range(n)])


# Tömbkezeléssel összefüggő segédfüggvények
###########################################

def vectPrint(F, fstr):
    "Vektor elemeinek az fstr stringben megadott formátum szerinti nyomtatása"
    n = len(F)
    for i in range(n):
        print(format(F[i],fstr))
    return

  
def matrPrint(W, fstr):
    "Mátrix elemeinek az fstr stringben megadott formátumú nyomtatása"
    # Ennek a függvénynek a bemete csak mátrix lehet
    nRow = len(W)
    nCol = len(W[0])
    for i in range(nRow):
        line = ""
        for j in range(nCol):
            line += format(W[i][j],fstr)
        print(line)
    return


def mPrint(W, fstr="12.4f"):
    "Vektor vagy mátrix elemeinek, az fstr stringben megadott formátumú nyomtatása"
    # A vectPrint és a matrPrint helyett használható
    # A bemenet vektor és mátrix is lehet
    try:
        nRow = len(W)
        try:
            nCol = len(W[0])
            for i in range(nRow):
                line = ""
                for j in range(nCol):
                    line += format(W[i][j],fstr)
                print(line)
        except:
            for i in range(nRow):
                print(format(W[i],fstr))
    except:
        print(format(W,fstr))
    return


def vectCopy(W):
    "Vektor másolása egy másik, új vektorba"
    # A paraméterként kapott vektor másolatát adja vissza egy új listában
    nRow = len(W)
    Save = DIM(nRow)
    for k in range(nRow):
        Save[k] = W[k]
    return(Save)


def matrCopy(W):
    "Mátrix másolása egy másik, új mátrixba"
    # A paraméterként kapott mátrix másolatát adja vissza egy új listában
    nRow = len(W)
    nCol = len(W[0])
    Save = DIM(nRow,nCol)    
    for k in range(nRow):
        for l in range(nCol):
            Save[k][l] = W[k][l]
    return(Save)


def mCopy(W):
    "Mátrix vagy vektor másolása egy másik új vektorba vagy mátrixba"
    # AvectCopy és a matrCopy helyett használható.
    # A másolandó vektos és mátrix is lehet
    nRow = len(W)
    try:
        nCol = len(W[0])
        Save = DIM(nRow,nCol)
        for k in range(nRow):
            for l in range(nCol):
                Save[k][l] = W[k][l]
    except:
        Save = DIM(nRow,1)
        for k in range(nRow):
            Save[k] = W[k]
    return(Save)


def mdRow(X,iBeg,iEnd):
    "Vektor (adatlista) adott sorszámokkal határolt tartományának kivágása"
    return(X[iBeg:iEnd])
        
    
def mdCol(W,iy,ix=[]):
    "Egy mátrixból adott indexű oszlopok leválogatása"
    # Mérési adatok feldolgozásánál használt fontos függvény
    # Segítségével lehet egy adatmátrixból a függő- és függetlenváltozókat kiválasztani
    # colList az a lista, amely a kiválasztandó oszlopok indexeit tartalmazza
    N =len(W)
    M = len(ix)
    #Független változók kiválasztása, ha volt ix megadva
    if( M!=0):
        if( M==1 ):
            wX = DIM(N)
            for i in range(N):
                wX[i] = W[i][ix[0]]   
        else:
            wX = DIM(N,M)
            for i in range(N):
                for j in range(M):
                    wX[i][j] = W[i][ix[j]]
    else:
        wX = []
    #Függő változó kiválasztása
    wY = DIM(N) 
    for i in range(N):
        wY[i] = W[i][iy]
    if( M==0 ):
        return(wY)
    else:
        return(wX,wY)
    

def vectMove(wX,wY,Index,op="col"):
    "Vektornak egy mátrix sorába vagy oszlopába másolása"
    # A mátrix Index-ben megadott sora vagy oszlopa a vektor elemeivel felűlírásra kerül
    nVect = len(wX)
    nMatr = len(wY)
    mMatr = len(wY[0])
    if( op=="col" ):
        if( nVect!=nMatr ):
            print("Nem megfelelő dimenzió")
            return
        for i in range(nVect):
            wY[i][Index] = wX[i]
        return
    if( op=="row" ):
        if( nVect!=mMatr ):
            print("Nem megfelelő dimenzió")
            return
        for i in range(nVect):
            wY[Index][i] = wX[i]
        return
    print("Nem megfelelő műveleti kód")
    return


def mConcat(wX,wY,op="Right"):
    "Vektorok és/vagy mátrixok összefűzése"
    nX = len(wX)
    nY = len(wY)
    try:
        mX = len(wX[0])
    except:
        mX = 1
    try:
        mY = len(wY[0])
    except:
        mY = 1
    if( op=="Right" ):
        nZ = mX+mY
        wZ = DIM(nX,nZ)
        if( mX==1 and mY==1 ):
            if( nX!=nY ):
                print("A vektorok nem egyenlő számú elemet tartalmaznak")
                return
            for i in range(nX):
                wZ[i][0] = wX[i]
            for i in range(nX):
                wZ[i][1] = wY[i]
            return(wZ)
        if( mX==1 and mY>1 ):
            if( nX!=nY ):
                print("A vektor elemeinek száma nem egyezik a mátrix sorai számával")
                return
            for i in range(nX):
                wZ[i][0] = wX[i]
            for i in range(nX):
                for j in range(mY):
                    wZ[i][mX+j] = wY[i][j]
            return(wZ)
        if( mX>1 and mY==1 ):
            if( nX!=nY ):
                print("A mátrix sorainak száma nem egyezik a vektor elemeinek számával")
                return
            for i in range(nX):
                for j in range(mX):
                    wZ[i][j] = wX[i][j]
            for i in range(nY):
                wZ[i][mX] = wY[i]
            return(wZ)
        if( mX>1 and mY>1 ):
            
            if( nX!=nY ):
                print("A mátrixok nem ozonos számú sort tartalmaznak")
                return
            for i in range(nX):
                for j in range(mX):
                    wZ[i][j] = wX[i][j]
            for i in range(nX):
                for j in range(mY):
                    wZ[i][mX+j] = wY[i][j]
            return(wZ)
    if( op=="Bottom" ):
        if( mX==1 and mY==1 ):
            wZ = DIM(2,nX)
            for i in range(nX):
                wZ[0][i] = wX[i]
            for i in range(nX):
                wZ[1][i] = wY[i]
            return(wZ)
        if( mX==1 and mY>1 ):
            if( nX!=mY ):
                print("A vektor és a mátrix nem azonos számú oszlopot tartalmaznak")
                return
            wZ = DIM(nY+1,nX)
            for i in range(nX):
                wZ[0][i] = wX[i]
            for i in range(nY):
                for j in range(mY):
                    wZ[1+i][j] = wY[i][j]
            return(wZ)
        if( mX>1 and mY==1 ):
            if( mX!=nY ):
                print("A vektor és a mátrix nem azonos számú oszlopot tartalmaznak")
                return
            wZ = DIM(nX+1,mX)
            for i in range(nX):
                for j in range(mX):
                    wZ[i][j] = wX[i][j]
            for i in range(mX):
                wZ[nX][i] = wY[i]
            return(wZ)
        if( mX>1 and mY>1 ):
            if( mX!= mY ):
                print("A két mátrix nem egyforma számú oszlopot tartalmaz")
                return
            wZ = DIM(nX+nY,mX)
            for i in range(nX):
                for j in range(mX):
                    wZ[i][j] = wX[i][j]
            for i in range(nY):
                for j in range(mY):
                    wZ[nX+i][j] = wY[i][j]
            return(wZ)
    print("Hibás operációs kód")
    return


def vectShift(x,n=1,move="right"):
    "Vektor elemeinek n pozícióval történő jobbra vagy balra léptetése"
    nx = len(x)
    if( move=="right" ):
        for i in range(n):
            a = x[nx-1]
            for j in range(nx-1,0,-1):
                x[j] = x[j-1]
            x[0] = a
        return(x)
    if( move=="left" ):
        for i in range(n):
            a = x[0]
            for j in range(1,nx):
                x[j-1] = x[j]
            x[nx-1] = a
        return(x)
    else:
        return(0)


def sgn(w):
    "Előjelfüggvény"
    if( w<0 ):
        return(-1)
    elif( w>0 ):
        return(1)
    else:
        return(0)


# Alapvető adatkezelési függvények
##################################

def mdInput():
    "Adatok beolvasása billentyűzetről"
    print("Mérési adatok beolvasása billentyűzetről")
    Title = input("Felirat, az adatok azonosítására szolgáló szöveg:")
    nCol =  int(input("Egy mérési ponthoz tartozó adatok száma:"))
    nRow = int(input("A mérési pontok száma:"))
    if( nCol==1 ):
        wD = [ 0 for i in range(nRow)]
        for i in range(nRow):
            w = "Data("+str(i)+"):"
            wD[i] = float(input(w))
        return(Title,nCol,nRow,wD)
    wD = [[0]*nCol for i in range(nRow)]
    for i in range(nRow):
        for j in range(nCol):
            w = "Data("+str(i)+","+str(j)+")="
            wD[i][j] = float(input(w))
    return (Title,nCol,nRow,wD)


def mdSave(fileName,Title,nCol,nRow,Data,fstr="10.4f"):
    "Mérési adatok mentése"
    # Mérési adatok mentése
    # fileName: az adatokat tartalmazó file neve
    # Title:    szöveg a tárolt adatok azonosítására
    # nCol:     egy adatponthoz tartozó értékek száma
    # nRow:     a tárolni kívánt adatpontok száma
    # Data:     a mérési adatokat tartalmazó mátrix (lista)
    f = open(fileName,'w')
    f.write(Title+"\n")
    f.write(str(nCol)+"\n")
    f.write(str(nRow)+"\n")
    if( nCol==1 ):
        for i in range(nRow):
            f.write(str(format(Data[i],fstr)+"\n"))
        return
    for i in range(nRow):
        d = ""
        if (nCol>1):
            for j in range(nCol-1):
                d = d+str(format(Data[i][j],fstr))+","
        else:
            j = -1
        d = d+str(format(Data[i][j+1],fstr))+"\n"
        f.write(d)
    f.close()
    return


def mdLoad(fileName):
    "Mérési adatok betöltése"
    f = open(fileName,"r")
    Title = f.readline()
    nCol = int(f.readline())
    nRow = int(f.readline())
    wX = []
    #Csak egy oszlop van           
    if( nCol==1 ):
        for i in range(nRow):
            wX.append(float(f.readline()))
        return(Title,nCol,nRow,wX)
    #Több oszlop van
    for i in range(nRow):
        ws = f.readline()
        wl = ws.split(",")
        wX.append([])
        for j in range(nCol):
            wX[i].append(float(wl[j]))
    return(Title,nCol,nRow,wX)


def mdReadCSV(fileName,delimiter=";"):
    "csv file beolvasása"
    # Tetszőleges karakterrel elválasztott, oszlopokból álló fájl beolvasása
    # fileName: beolvasandó file neve
    # delimiter: az egyes oszlopokat elválasztó karakter
    wX = []
    Fejlec = []
    n = 0
    file = open(fileName,"r")
    sor = file.readline()
    w = sor.split(delimiter)
    m = len(w)
    try:
        wX.append([])
        for i in range(m):
            wX[n].append(float(w[i]))
        n += 1
    except (ValueError):
        if( sor.endswith("\n")):
            sor = sor.rstrip("\n")
        Fejlec = sor.split(delimiter)
        wX = []
    Tartalom = file.readlines()
    for sor in Tartalom:
        w = sor.split(delimiter)
        m = len(w)
        wX.append([])
        for i in range(m):
            wX[n].append(float(w[i]))
        n += 1
    return(Fejlec,n,m,wX)


# Rajzolási függvények, a Tkinter használatával
##############################################

def Axes(size,subtitles,xlimits,ylimits,origo,scale,afrm=["",""]):
    "Rajzolási terület beállítása és tengelyek rajzolása"
    # size:      fizikai terület
    # subtitles: az ablak neve és a rajz tetején megjelenő felirat
    # xlimits:   független változó értéktartománya
    # ylimits:   függő változó értékkészlete
    # origo:     a tengelyek metszéspontja
    # scale:     a tengelyek beosztása

    # Tengelyek színének beállítása
    acolor = "black"
    
    # Létrehozzuk az ábrát
    selfxs = size[0]
    selfys = size[1]
    title = subtitles[0]
    text = subtitles[1]
    master = Tk()
    # Az ablak nevének megadása
    master.title(title)
    myCanvas = Canvas(master, width=selfxs, height=selfys)
    myCanvas.pack()
    # A rajz tetején megjelenő szöveg
    # A text elhelyezésének irányai a földrajzi irányokat követi (nw,n,ne,w,center,e,sw,s,se)
    canvas_id=myCanvas.create_text(10,10,anchor="n")
    myCanvas.create_text(700,30,text=text)
    # Korben megnoveljuk a rajzteruletet (vizualisan jobban befogadhato)
    xmin = xlimits[0]
    xmax = xlimits[1]
    xpad = (xmax-xmin)*0.09
    xmin = xmin - xpad
    xmax = xmax + xpad
    
    ymin = ylimits[0]
    ymax = ylimits[1]
    ypad = (ymax-ymin)*0.09
    ymin = ymin - ypad
    ymax = ymax + ypad

    selfxbias = (0-xmin)
    selfybias = (0-ymin)
    
    selfxstep = selfxs/(xmax-xmin)
    selfystep = selfys/(ymax-ymin)

    # tengelyek rajzolása
    horY  = origo[1]
    vertX = origo[0]
    line(myCanvas,xlimits[0],horY,xlimits[1],horY,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,color=acolor)
    line(myCanvas,vertX,ylimits[0],vertX,ylimits[1],selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,color=acolor)

    # osztások tervezese es kirajzolasa
    xpos = xlimits[0]
    xstep = scale[0]
    xfstr = afrm[0]
    yticks = abs(ymax-ymin)/100                
    while( xpos<=xlimits[1] ):
        line(myCanvas,xpos,horY-yticks,xpos,horY+yticks,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,acolor)
        if( xfstr!="" ):
            ptext(myCanvas,xpos,horY-2*yticks,format(xpos,xfstr),selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias)
        xpos += xstep
        
    xticks = abs(xmax-xmin)/100                
    ypos = ylimits[0]
    ystep = scale[1]
    yfstr = afrm[1]
    while( ypos<=ylimits[1] ):
        line(myCanvas,vertX-xticks,ypos,vertX+xticks,ypos,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,acolor)
        if( yfstr!="" ):
            ptext(myCanvas,vertX+1.55*xticks,ypos,format(ypos,yfstr),selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias)
        ypos += ystep

    # visszatérés   
    axes = [myCanvas,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias]       
    return( axes )


def autoAxes(size,xlimits,ylimits):
    "Rajzolási terület beállítása és a tengelyek automatikus felrajzolása"
    # Automatikusan keresi meg az origot és állítja be a tngely osztásokat
    
    # Fizikai rajzolási terület létrehozása
    selfxs = size[0]
    selfys = size[1]
    master = Tk(screenName="Próba rajzterület")
    myCanvas = Canvas(master, width=selfxs, height=selfys)
    myCanvas.pack()
    
    # Korben megnoveljuk a rajzteruletet (vizualisan jobban befogadhato)
    xmin = xlimits[0]
    xmax = xlimits[1]
    xpad = (xmax-xmin)*0.05
    xmin = xmin - xpad
    xmax = xmax + xpad
    
    ymin = ylimits[0]
    ymax = ylimits[1]
    ypad = (ymax-ymin)*0.05
    ymin = ymin - ypad
    ymax = ymax + ypad
    
    selfxbias = (0-xmin)
    selfybias = (0-ymin)
    
    selfxstep = selfxs/(xmax-xmin)
    selfystep = selfys/(ymax-ymin)

    # A tengelyeknel az eredeti ertekek szuksegesek es nem a novelt
    if((xlimits[1]*xlimits[0]) < 0): # ha negativ, akkor a nulla a ket vegpont kozott van
        vertX = 0
    else:
        vertX = xlimits[0]

    if((ylimits[1]*ylimits[0]) < 0):
        horY = 0
    else:
        horY = ylimits[0]
    
    line(myCanvas,xlimits[0],horY,xlimits[1],horY,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,color="blue")
    line(myCanvas,vertX,ylimits[0],vertX,ylimits[1],selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,color="blue")

    # osztások tervezese es kirajzolasa
    (xstep, xstart) = calcTicks(xmin, xmax)
    (ystep, ystart) = calcTicks(ymin, xmax)
        
    yticks = abs(ymax-ymin)/100                
    xpos = xstart
    while(xpos < (xmax+xstep)):
        line(myCanvas,xpos,horY-yticks,xpos,horY+yticks,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,"blue")
        self.text(xpos,horY-2*yticks,format(xpos,"6.1f"))
        xpos = xpos+xstep

    xticks = abs(xmax-xmin)/100                
    ypos = ystart
    while(ypos < (ymax+ystep)):
        line(myCanvas,vertX-xticks,ypos,vertX+xticks,ypos,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias,"blue")
        self.text(vertX+1.5*xticks,ypos,format(ypos,"6.1f"))
        ypos = ypos+ystep
    axes = [myCanvas,selfxs,selfys,selfxstep,selfystep,selfxbias,selfybias]       
    return( axes )


def calcTicks(minval, maxval):
    diffval = maxval-minval
    logdiff = log(diffval)/log(10)
    logint = floor(logdiff)
    stepval = pow(10,logint-1)
    startval = stepval*floor(minval/stepval)   
    return (stepval, startval)


def dPlot(plotParam,x,y,plotType="dot",color="red"):
    "Az x és y vektorokban adott függvényértékek kirajzolása"

    Canvas = plotParam[0]
    selfxs = plotParam[1]
    selfys = plotParam[2]
    xstep  = plotParam[3]
    ystep  = plotParam[4]
    xbias  = plotParam[5]
    ybias  = plotParam[6]

    N = len(x)  # kirajzolandó pontok száma

    if( plotType == "line" ):
        for i in range(N-1):
            line(Canvas,x[i],y[i],x[i+1],y[i+1],selfxs,selfys,xstep,ystep,xbias,ybias,color=color)
    elif( plotType == "dot" ):
        for i in range(N):
            point(Canvas,x[i],y[i],selfxs,selfys,xstep,ystep,xbias,ybias,color=color)
    else:
        print("Ismeretlen rajzolási forma!")
        return
    return


def fPlot(plotParam,vX,FNY,color="red"):
    "Az FNY függvény értékeinek folyamatos vonallal történő felrajzolása a vX-ben megadott pontokban"
    # vX[0]: független változó kezdeti értéke
    # vX[1]: független változó legnagyobb értéke
    # vX[2]: független váétozó lépésköz
    # FNY: az ábrázolandó függvény
    Canvas = plotParam[0]
    selfxs = plotParam[1]
    selfys = plotParam[2]
    xstep  = plotParam[3]
    ystep  = plotParam[4]
    xbias  = plotParam[5]
    ybias  = plotParam[6]

    x0 = vX[0]
    y0 = FNY(x0)
    x  = x0+vX[2]
    while( x<=vX[1] ):
        y = FNY(x)
        line(Canvas,x0,y0,x,y,selfxs,selfys,xstep,ystep,xbias,ybias,color=color)
        x0 = x
        y0 = y
        x += vX[2]
    return

         
def line(myCanvas,xs,ys,xe,ye,sxs,sys,xstep,ystep,xbias,ybias,color="black"):
    # c = az aktuális Canvas
    xsc = (xs+xbias)*xstep
    ysc = sys-(ys+ybias)*ystep
    xec = (xe+xbias)*xstep
    yec = sys-(ye+ybias)*ystep
    myCanvas.create_line(xsc,ysc,xec,yec,fill=color)
    return


def ptext(myCanvas,xs,ys,txt,sxs,sys,xstep,ystep,xbias,ybias):
    xsc = (xs+xbias)*xstep
    ysc = sys-(ys+ybias)*ystep
    myCanvas.create_text(xsc,ysc,text=txt)
    return

def point(myCanvas,xs,ys,sxs,sys,xstep,ystep,xbias,ybias,color="black"):
    xsc = (xs+xbias)*xstep
    ysc = sys-(ys+ybias)*ystep
    stick = 5
    myCanvas.create_line(xsc-stick,ysc,xsc+stick,ysc,fill=color)
    myCanvas.create_line(xsc,ysc-stick,xsc,ysc+stick,fill=color)
    return


def exportPlot(axes,fileName,colorMode="color"):
    "Rajz exportálása post script formátumban"
    myCanvas = axes[0]
    myCanvas.update()
    myCanvas.postscript(file=fileName+".ps", colormode='color')
    return
 


#Vektorokon és mátrixokon értelmezett műveletek
################################################

def vectScal(s,w):
    "Vektornak skalárral történő szorzása"
    b = []
    n = len(w)
    for i in range(n):
        b.append(w[i]*s)
    return(b)


def matrScal(s,wX):
    "Mátrixnak skalárral történő szorzása"
    
    nX = len(wX)
    mX = len(wX[0])
    W = []
    for i in range(nX):
        W.append([])
        for j in range(mX):
            W[i].append(s*wX[i][j])
    return(W)


def mScal(s,wX):
    "Egy tömb(vektor vagy mátrix) minden elemének skalárral történő szorzása"
    nX = len(wX)
    try:
        mX = len(wX[0])
        W = DIM(nX,mX)
        for i in range(nX):
            for j in range(mX):
                W[i][j] = s*wX[i][j]
    except:
        W = DIM(nX)
        for i in range(nX):
            W[i] = s*wX[i]
    return( W )


def vectAdd(x,y):
    "Vektorok összeadása"
    # Ebben a függvényben nem használjuk a DIM utasítást !!!!!!!!
    # Azt kívánjuk szemléltetni, hogy lehet egy algoritmusban folyamatosan
    # építeni egy listát
    w = []
    nX = len(x)
    nY = len(y)
    if nX != nY:
        print("A megadott két vektor hossza nem egyezik")
        return([])
    for i in range(nX):
        w.append(x[i] + y[i])
    return(w)


def matrAdd(wX,wY):
    "Mátrixok összeadása"
    nX = len(wX)
    mX = len(wX[0])
    nY = len(wY)
    mY = len(wY[0])
    if (nX != nY) or (mX != mY):
        print("A két mátrix nem azonos dimenziójú!")
        return([])
    W = []
    for i in range(nX):
        W.append([])
        for j in range(mX):
            W[i].append(wX[i][j]+wY[i][j])
    return(W)
  

def vectSub(x,y):
    "Vektorok különbsége"
    w = []
    nX = len(x)
    nY = len(y)
    if nX != nY:
        print("A két vektor hossza nem egyezik")
        return([])
    for i in range(nX):
        w.append(x[i] - y[i])
    return(w)


def matrSub(wX,wY):
    "Mátrixok különbsége"
    nX = len(wX)
    mX = len(wX[0])
    nY = len(wY)
    mY = len(wY[0])
    W = []
    if (nX != nY) or (mX != mY):
        print("A két mátrix nem azonos dimenziójú!")
        return([])
    for i in range(nX):
        W.append([])
        for j in range(mX):
            W[i].append(wX[i][j]-wY[i][j])
    return(W)


def mAdd(wX,wY,op="add"):
    "Két mártix vagy vektor összege vagy különbsége"
    err = "mAdd: Nem egfelelő dimenziók!"
    if( op!="add" and op!="sub" ):
        print("mAdd: Hibás operációs kód")
        return( [] )
    pos = DIM(2)
    nX = len(wX)
    nY = len(wY)
    try:
        mX = len(wX[0])
        pos[0] = "m"
    except:
        pos[0] = "v"
    try:
        mY = len(wY[0])
        pos[1] = "m"
    except:
        pos[1] = "v"
    if( pos[0]=="m" and pos[1]=="m" ):
        # Két mátrix elemeinek az összege
        if( nX!=mY and mX!=mY ):
            print(err)
            return( [] )
        W = DIM(nX,mY)
        for i in range(nX):
            for j in range(mY):
                if( op=="add" ):
                    W[i][j] = wX[i][j]+wY[i][j]
                else:
                    W[i][j] = wX[i][j]-wY[i][j]
        return( W ) # A visszatérőérték egy mátrix
    if( pos[0]=="v" and pos[1]=="v" ):
        # két vektor elemeinek az összege
        if( nX != nY ):
            print(err)
            return([])
        z=DIM(nX)
        for i in range(nX):
            if( op=="add" ):
                z[i] = wX[i]+wY[i]
            else:
                z[i] = wX[i]-wY[i]
        return( z ) # A visszatérési érték egy vektor


def vectDot(x,y):
    "Vektorok skaláris szorzata"
    nX = len(x)
    nY = len(y)
    if nX != nY:
        print("A két vektor hossza nem egyezik")
        return([])
    w = 0.0
    for i in range(nX):
        w += x[i]*y[i]
    return(w)


def matrMvect(wX,wy):
    "Mátrixnak vektorral jobbról történő szorzása"
    nnX = len(wX[0])
    nX = len(wX)
    ny = len(wy)
    if (nnX != ny):
        print("Nem egfelelő dimenziók")
        return(0)
    w = []
    for i in range(nX):
        s = 0.0
        for j in range(ny):
            s += wX[i][j]*wy[j]
        w.append(s)
    return(w)


def matrMult(wX,wY):
    "Mátrixok szorzása"
    nX = len(wX)
    mX = len(wX[0])
    nY = len(wY)
    mY = len(wY[0])
    if (mX != nY):
        print("Nem megfelelő dimenziók")
        return([])
    W = []
    for i in range(nX):
        W.append([])
        for j in range(mY):
            s = 0.0
            for k in range(mX):
                s += wX[i][k]*wY[k][j]
            W[i].append(s)
    return(W)


def mMult(wX,wY):
    "Vektorok és Mátrixok szorzása"
    # (vektor,vektor), (vektor,mátrix), (mátrix, mátrix)
    # (szám, vektor) (szám,szám) szorzás
    err = "mMult: Nem egfelelő dimenziók!"
    pos = [" "," "]
    try:
        nX = len(wX)
    except:
        pos[0] = "s"
        s = wX
    try:
        nY = len(wY)
    except:
        pos[1] = "s"
        s = wY
    if( pos[0]!="s" ):
        try:
            mX = len(wX[0])
            pos[0] = "m"
        except:
            pos[0] = "v"
    if( pos[1]!="s" ):
        try:
            mY = len(wY[0])
            pos[1] = "m"
        except:
            pos[1] = "v"
    if( pos[0]=="m" and pos[1]=="m" ):
        # Két mátrix szorzata
        if( mX!=nY ):
            print(err)
            return( [] )
        W = DIM(nX,mY)
        for i in range(nX):
            for j in range(mY):
                s = 0.0
                for k in range(mX):
                    s += wX[i][k]*wY[k][j]
                W[i][j] = s
        return( W ) # A visszatérőérték egy mátrix
    if( pos[0]=="v" and pos[1]=="v" ):
        # Két vektor skaláris szorzata
        if( nX != nY ):
            print(err)
            return([])
        s = 0.0
        for i in range(nX):
            s += wX[i]*wY[i]
        return(s) # A visszatérési érték egy szám
    if( (pos[0]=="v" and pos[1]=="m") or (pos[0]=="m" and pos[1]=="v" ) ):
        # Egy mátrix és egy vektor szorzata
        if( pos[0]=="v" and pos[1]=="m"):
            if( nX!=mY ):
                print(err)
                return( [] )
            z = mCopy(wX)
            Z = mCopy(wY)
        if( pos[0]=="m" and pos[1]=="v" ):
            if( mX!= nY ):
                print(err)
                return( [] )
            z = mCopy(wY)
            Z = mCopy(wX)
        nz = len(z)
        nZ = len(Z)
        w = DIM(nz)
        for i in range(nZ):
            s = 0.0
            for j in range(nz):
                s += Z[i][j]*z[j]
            w[i] = s
            # A visszatérési érték egy vektor
        return( w )
    if( (pos[0]=="s" and pos[1]=="v") or (pos[0]=="v" and pos[1]=="s" )):
        # Egy szám és egy vektor szorzata
        if( pos[0]=="s" and pos[1]=="v" ):
            w = DIM(nY)
            for i in range(nY):
                w[i] = s*wY[i]
            # A visszatérési érték egy vektor
            return( w )
        if( pos[0]=="v" and pos[1]=="s" ):
            w = DIM(nX)
            for i in range(nX):
                w[i] = s*wX[i]
            # A visszatérési érték egy vektor
            return( w )
    if( (pos[0]=="s" and pos[1]=="m") or (pos[0]=="m" and pos[1]=="s" )):
        # Egy szám és egy mátrix szorzata
        if( pos[0]=="s" and pos[1]=="m" ):
            w = DIM(nY,mY)
            for i in range(nY):
                for j in range(mY):
                    w[i][j] = s*wY[i][j]
            # A visszatérési érték egy mátrix
            return( w )
        if( pos[0]=="m" and pos[1]=="s" ):
            w = DIM(nX,mX)
            for i in range(nX):
                for j in range(mX):
                    w[i][j] = s*wX[i][j]
            # A visszatérési érték egy mátrix
            return( w )
    if( pos[0]=="s" and pos[1]=="s" ):
        # Két szám szorzata
        return( wX*wY )

            
# Vektorokon értelmezett műveletek
def vectAbs(wX, fstr="12.4f"):
    "Vektor maximális abszolút értékű eleme"
    n = len(wX)
    w = mCopy(wX)
    for i in range(n):
        w[i] = abs(w[i])
    return( max(w) )


def vectLen(x):
    "Vektor hossza (abszolút értéke)"
    # Ez nem a Python len függvénye, amely egy lista hosszát adja vissza!!!!!!!!
    c = 0.0
    nX = len(x)
    for i in range(nX):
        c += x[i] * x[i]
    c = sqrt(c)
    return(c)


def vectAngl(x,y):
    "Két vektor által bezárt szög"
    dot = vectDot(x,y)
    lenX = vectLen(x)
    lenY = vectLen(y)
    e = acos(dot/(lenX*lenY))
    return(e)


#Mátrixokon értelmezett műveletek
def matrDiag(n,val=1):
    "n dimenziós diagonálmátrix létrehozása, az átlóban val értékkel feltöltve"
    W = DIM(n,n)    
    for i in range(n):
        W[i][i] = val
    return(W)


def matrTrans(wX):
    "Mátrix transzponálása"
    n = len(wX)
    m = len(wX[0])
    wZ = DIM(m,n)
    for j in range(m):
        for i in range(n):
            wZ[j][i] = wX[i][j]
    return(wZ)


def matrEukl(wX):
    "Mátrix abszolútértéke"
    nX = len(wX[0])
    mX = len(wX)
    e = 0.0
    for i in range(0,nX):
        for j in range(mX):
            e += wX[i][j]*wX[i][j]
    return(sqrt(e))


def matrGauss(X,y):
    "Lineáris egyenletrendszer megoldása Gauss-Jordan módszerrel"
    N = len(X)
    M = N+1 
    wX = []
    wX = mCopy(X)
    nom = 0
    for i in range(N):
        wX[i].append(y[i])   
    for j in range(N):
        for i in range(j,N):
            nom = 0
            if (wX[i][j] != 0):
                nom = 1
                break
        if (nom==0):
            return(DIM(N))
        for k in range(N+1):
            s = wX[j][k]
            wX[j][k] = wX[i][k]
            wX[i][k] = s
        t = 1/wX[j][j]
        for k in range(N+1):
            wX[j][k] = t*wX[j][k]
        for l in range(N):
            if ( l==j):
                continue # i szerint
            t = -1*wX[l][j]
            for k in range(N+1):
                wX[l][k] = wX[l][k]+t*wX[j][k]    
    w = []
    for i in range(N):
        w.append(wX[i][N])    
    return (w)


def matrInv(X):
    "Mátrix inverzének meghatározása Gauss_Jordan módszerrel"
    N = len(X)
    wX = matrCopy(X)
    # Egységmátrix létrehozása
    W = matrDiag(N,1)
    nom = 0
    # A Gauss - Jordan eljárás
    for j in range(0,N):
        nom = 0
        for i in range(j,N):
            if (wX[i][j] != 0):
                nom = 1
                break
            
        if( nom==0):
            print("det(A)=0")
            return (DIM(N,N))
        
        for k in range(N):
            s = wX[j][k]
            wX[j][k] = wX[i][k]
            wX[i][k] = s
            s = W[j][k]
            W[j][k] = W[i][k]
            W[i][k] = s
        
        t = 1/wX[j][j]
        for k in range(N):
            wX[j][k] = t*wX[j][k]
            W[j][k] = t*W[j][k]
        
        for l in range(0,N):
            if ( l==j ):
                continue # i szerint
            t = -1*wX[l][j]
            for k in range(N):
                wX[l][k] = wX[l][k]+t*wX[j][k]
                W[l][k] = W[l][k]+t*W[j][k]
    return (W)


# Speciális mátrixfüggvények
def matrEigen(A,eps=1e-5):
    "Mátrix maximális sajértékének és a hozzá tartozó sajátvektor meghatározása"
    N = len(A)
    wA = mCopy(A)
    wB = DIM(N,1,1/sqrt(N))
    b = 1
    nstep = 0
    a = 1000
    while ( abs((a-b)/a)>eps ):
        b = a
        a = 0
        wB = matrMvect(wA,wB)
        for i in range(0,N):
            a = a+wB[i]*wB[i]
            nstep = nstep+1
        a = sqrt(a)
        for i in range(0,N):
            wB[i] = wB[i]/a
    return (wB,a)


def matrExp(E,x):
    "Mátrix x. hatványra emelése"
    maxTerms = 1000     #Az iteráció maximális száma
    n = len(E)
    wD = DIM(n,n)
    wB = matrDiag(n,1)
    wC = mCopy(wB)
    wD = mAdd(wD,wC)
    Terms = 1
    while( Terms<maxTerms):
        W = mCopy(E)
        b = x/Terms
        W = mMult(b,W)
        wC = mMult(W,wB)
        wD = mAdd(wD,wC)
        wB = mCopy(wC)
        Terms = Terms+1
    return(wD)


# Mérési adatok feldolgozását segítő függvények
###############################################

def setList(xmin,xmax,xstep):
    "Egy lista értékekkel történő feltöltése Min-től - Max-ig, Step lépésenként"
    wX = []
    x = xmin
    while( x<=xmax ):
        wX.append(x)
        x += xstep
    return(wX)


def evalFunc(P,FNY,p=[]):
    "Egyváltozós függvény értékeinek kiszámítása adott független változó értékekre"
    # P[0]: alsó határ; P[1]: felső határ; P[2]: növekmény
    # Ha a p nem tartalmaz elemet, akkor az FNY függvény csak az x-től függ
    # Ha a p tartalmaz elemet, akkor az az FNY részére átadásra kerül
    # Az egyedi függvény megírásakor kell gondoskodni a paraméterek megfelelő kezeléséről
    wX = []
    wY = []
    x = P[0]
    while( x<=P[1] ):
        if( len(p)==0 ):
            wY.append(FNY(x))
        else:
            wY.append(FNY(x,p))
        wX.append(x)
        x += P[2]
    return( wX,wY )


def evalPFunc(wX,FNY,p=[]):
    "Egyváltozós függvény értékeinek kiszámítása egy listában adott független változó értékekre"
    # wX: A függetlenváltókat tartalmazó lista
    # Ha a p nem tartalmaz elemet, akkor az FNY függvény csak az x-től függ
    # Ha a p tartalmaz elemet, akkor az az FNY részére átadásra kerül
    # Az egyedi függvény megírásakor kell gondoskodni a paraméterek megfelelő kezeléséről
    N = len(wX)
    wY = DIM(N)
    for i in range(N):
        if( len(p)==0 ):
            wY[i] = FNY(wX[i])
        else:
            wY[i] = FNY(wX[i],p)
    return( wY )


def mdPolyval(p,wX):
    "n-ed fokú polinom értékének kiszámítása"
    n = len(p)
    try:
        N = len(wX)
    except:
        s = p[n-1]*wX
        for j in range(n-2,0,-1):
            s = wX*(p[j]+s)
        return( s+p[0] )
    wY = DIM(N)
    for i in range(N):
        s = p[n-1]*wX[i]
        for j in range(n-2,0,-1):
            s = wX[i]*(p[j]+s)
        wY[i]= s+p[0]
    return( wY )

    
def mdRacval(r,p,a,wX):
    "Racionális törtfüggvény értékének kiszámítása"
    wY = []
    for i in range(len(wX)):
        wR=wP=0
        wR = a[r]*wX[i]
        for k in range(r-1,0,-1):
            wR =wX[i]*(wR+a[k])
        wR += a[0]
        wP = a[r+p]*wX[i]
        for k in range(r+p-1,r,-1):
            wP = wX[i]*(wP+a[k])
        wY.append(wR/(1+wP))
    return(wY)


def mdTrigpol(wX,nSin,nCos,p,alfa=1):
    "Trigonometrikus polinom értékeinek kiszámítása"
    N = len(wX)
    wY = []
    for i in range(N):
        s = p[0]
        for j in range(nSin):
            s += p[j+1]*sin(alfa*(j+1)*wX[i])
        for j in range(nCos):
            s += p[nSin+j+1]*cos(alfa*(j+1)*wX[i])
        wY.append(s)
    return( wY )            

                         
# Alapvető statisztikai jellemzőket meghatározó függvény
########################################################
def mdBstat(wX, Itl=[]):
    "(Alapvető statisztikai jellemzők meghatározása"
    N = len(wX)
    w = vectCopy(wX)
    w.sort()
    Min = w[0]
    Max = w[N-1]
    R = Max-Min
    nI = len(Itl)
    s = DIM(nI)
    k = 0
    if( nI!=0 ):
        for j in range(k,N):
            for i in range(nI):
                if( Itl[i][0]<=w[j] and w[j]<Itl[i][1] ):
                    s[i] += 1
                    k = j
    # nincs megadott intervallum sorozat, minden értéket egyedileg kell vizsgálni
    elif( nI==0 ):
        s = []
        s.append([])
        s[0].append(w[0])
        s[0].append(1)
        j = 0
        for i in range(1,N):
            if( w[i] == w[i-1]):
                s[j][1] = s[j][1]+1
            else:
                j += 1
                s.append([])
                s[j].append(w[i])
                s[j].append(1)
        for i in range(j+1):
            s[i][1] = s[i][1]/N
    # Medián
    if( N%2==0 ):
        Med = (w[int(N/2-1)]+w[int(N/2+1)])/2
    else:
        Med = w[int(N/2)]
    # Átlag
    a = sum(wX)/N
    # Szórás
    si = 0
    for i in range(N):
        si += (wX[i]-a)**2
    si = sqrt(si/(N-1))      
    return(w,Min,Max,R,Med,a,si,s)


def mdLinfit(wX,wY,Type="LinLin",Title=[],fileName=""):
    "Lineáris és lineárisra visszavezethető regresszió"
    # Ha van cím megadva, akkor az eredmények nyomtatásra is kerülnek
    # Ha van fájlnév megadva, akkor az eredmények kimentésre kerülnek.
    N = len(wX)
    wx = matrNULL(N,1)
    wy = matrNULL(N,0)
    if( Type== "LinLin"):
        # Mind a két tengely lineáris
        sX = sY = 0.0
        for i in range(N):
          wx[i] = wX[i]
          wy[i] = wY[i]
    elif( Type=="LinLog" ):
        # Lineáris X és logaritmikus Y tengely
        sX = sY = 0.0
        for i in range(N):
          wx[i] = wX[i]
          wy[i] = log(wY[i])
    elif( Type=="LogLin" ):
        # Logaritmikus X és lineáris Y tengely
        sX = sY = 0.0
        for i in range(N):
          wx[i] = log(wX[i])
          wy[i] = wY[i]
    elif( Type=="LogLog" ):
        # Logaritmikus X és logaritmikus Y tengely
        sX = sY = 0.0
        for i in range(N):
          wx[i] = log(wX[i])
          wy[i] = log(wY[i])
    else:
        return(0,0,0)

    aX = sum(wx)/N
    aY = sum(wy)/N
    ssX = ssY = smd = 0.0
    
    for i in range(N):
        dX = wx[i]-aX
        dY = wy[i]-aY
        smd += dX*dY
        ssX += dX**2
        ssY += dY**2
    B = smd/ssX
    A = aY-B*aX
    R = smd/sqrt(ssX*ssY)
    CY = matrNULL(N,2)
    for i in range(N):
        CY[i][0]=A+B*wX[i]
        CY[i][1] = abs(wY[i]-CY[i][0])
    if( len(Title)!=0 ):
        # Az eredmények nyomtatása
        fN = "Polinom"
        precData = "14.4f"
        precCoef = "7.4f"
        prd = '%'+precData+'\t\t%'+precData+'\t\t%'+precData+'\t\t%'+precData
        #A pillanatnyi dátum és idő lekérése és formázása
        ido = datetime.now
        ido = ido.strftime("%Y-%m-%d %H:%M%S")
        # Az f" -string alkalmazasaval
        #tdt = f"{datetime.today():%Y-%B-%d  %H:%M}"
        print(Title)
        print("Közelítőfüggvény: Lineáris regresszió\n")
        print("Koordináta transzformáció: ",Type,"\n")
        print("Együtthatók:")
        print("a:%10.5f\nb:%10.5f" %(A,B))
        print('\nKorrelációs együttható:%6.4f\n' %R)
    # A közelített értékek nyomtatása, ha kell
        print("         X             Y             cY           deltaY ")
        for i in range(N):
            prs = format(wX[i],precData)
            prs += format(wY[i],precData)
            prs += format(CY[i][0],precData)
            prs += format(CY[i][1],precData)
            print(prs)
    # Az eredmények fájlba írása
    if( len(fileName)!=0 ):
        f = open(fileName,'w')
        f.write("Mérési adatok közelítése a legkisebb négyzetek módszerével   "+ido+"\n\n")
        f.write(Title+"\n")
        f.write("Közelítőfüggvény: Lineáris regresszió\n")
        f.write("Koordináta transzformáció: "+Type+"\n")
        f.write("Együtthatók:")
        f.write("\na:"+format(A,precCoef)+"\nb:"+format(B,precCoef))
        f.write("\nKorrelációs együttható:"+format(R,"6.4f"))
        f.write("\n\n")
        f.write("         X             Y             cY           deltaY \n")
        for i in range(N):
            prs = format(wX[i],precData)
            prs += format(wY[i],precData)
            prs += format(CY[i][0],precData)
            prs += format(CY[i][1],precData)
            f.write(prs+"\n")
    return(A,B,R)
        


def mdCorrcoef(wX):
    "Egy két oszlopból álló mátrix két oszlopa közötti korrelációs együttható"
    N = len(wX)
    sY = sX = 0.0
    for i in range(N):
        sX += wX[i][0]
        sY += wX[i][1]
    ssX = ssY = smd = 0.0
    aX = sX/N
    aY = sY/N
    for i in range(N):
        dX = wX[i][0]-aX
        dY = wX[i][1]-aY
        smd += dX*dY
        ssX += dX**2
        ssY += dY**2
    R = smd/sqrt(ssX*ssY)
    return(R)


def mdCorrcoeff(wX,wY):
    "Két független listaként (vektorként) megadott változók közötti korrelációs együttható"
    N = len(wX)
    aX = sum(wX)/N
    aY = sum(wY)/N
    ssX = ssY = smd = 0.0
    for i in range(N):
        dX = wX[i]-aX
        dY = wY[i]-aY
        smd += dX*dY
        ssX += dX**2
        ssY += dY**2
    R = smd/sqrt(ssX*ssY)
    return(R)


def mdPolyfit(wX,wY,n,Title="",fileName=""):
    "Mérési adatok közelítése n-ed fokú polinommal, a legkisebb négyzetek módszerével"
    # p az n-ed fokú polinom együtthatói
    # r := standard deviáció
    m = len(wX)
    n += 1
    p = DIM(n)
    if( m!=len(wY) ):
        print("Polyfit: Az x és y eltérő számú adatpontot tartalmaznak")
        return([],0)
    if( m<n-1 ):
        print("Polyfit: A közelítéshez kevés adatpont áll rendelkezésre")
        return([],0)
    wZ = DIM(m,n)
    for i in range(m):
        b = 1
        for j in range(n):
            wZ[i][j] = b
            b = b*wX[i]
    tZ = matrTrans(wZ)
    wA = matrMult(tZ,wZ)
    wy = matrMvect(tZ,wY)
    p = matrGauss(wA,wy)
    wy = mdPolyval(p,wX)
    r = mdCorrcoeff(wY,wy)
    # Az eredmények nyomtatása
    if( len(Title)!=0 ):
        precData = "14.4f"
        precCoef = "7.4f"
        prd = '%'+precData+'\t\t%'+precData+'\t\t%'+precData+'\t\t%'+precData
        #A pillanatnyi dátum és idő lekérése és formázása
        ido = datetime.now()
        ido = ido.strftime("%Y-%m-%d %H:%M%S")
        #tdt = f"{datetime.today():%Y-%B-%d  %H:%M}"
        print(Title)
        print("Közelítőfüggvény: Polinom\n")
        print("Együtthatók:")
        mPrint(p,precCoef)
        print("\nKorrelációs együttható:"+format(r,"6.4f")+"\n")
    # A közelített értékek nyomtatása, ha kell
        N = len(wX)
        print("         X             Y             cY           deltaY ")
        for i in range(N):
            prs = format(wX[i],precData)
            prs += format(wY[i],precData)
            prs += format(wy[i],precData)
            prs += format(abs(wY[i]-wy[i]),precData)
            print(prs)
    # Az eredmények fájlba írása
    if( len(fileName)!=0 ):
        f = open(fileName,'w')
        f.write("Mérési adatok közelítése a legkisebb négyzetek módszerével   "+ido+"\n\n")
        f.write(Title+"\n")
        f.write("Közelítőfüggvény: Polinom\n")
        f.write("Együtthatók:")
        for i in range(len(p)):
            f.write("\n"+format(p[i],precCoef))
        f.write("\nKorrelációs együttható:"+format(r,"6.4f"))
        f.write("\n\n")
        f.write("         X             Y             cY           deltaY \n")
        for i in range(N):
            prs = format(wX[i],precData)
            prs += format(wY[i],precData)
            prs += format(wy[i],precData)
            prs += format(abs(wY[i]-wy[i]),precData)
            f.write(prs+"\n")
    return(p,r)
    

def mdFocus(wy,nf,S=[1,2,1]):
    "Mérési hibákkal terhelt pontsorozat simítása"
    # Az msSmooth függvénnyel együtt használható !!!!!
    # wy: a simítandó függvényértékeket (ordináták) tartalmazó vektor
    # nf: az egymás utáni simítások száma
    # S:= a súlyok sorozata, amelynek páratlan számú elemet kell tartalmaznia
    # szimmetrikusan tartalmazza a súlyokat
    nS = len(S)
    s = sum(S)
    n = len(wy)
    if( nS<3 ):
        print("A figyelembe veendő pontok száma kisebb mint 1!")
        return(0,0)
    ns = nS//2
    if( nS%2==0 ):
        print("A súlyok sorozata nem páratlan számú!")
        return(0,0)
    wry = mCopy(wy)
    for i in range(nf):
        for j in range(nS,n-nS-1):
            ws = 0
            l = 0
            for k in range(j-ns,j+ns+1):
                ws += wy[k]*S[l]
                l += 1
            wy[j] = ws/s
    # Vége a pontsorozat simításának
    average = 0
    delta = 0
    for i in range(n):
        d = abs(wy[i]-wry[i])
        average += d
        if( d-delta>0 ):
            delta = d
    average /= n
    return(average,delta)
def mdSmooth(wX,wY,nf,tol,S=[1,2,1]):
    "Heurisztikus simító eljárás"
    # Az mdFocus kezelését végző eljárás
    # Egy méréssorozat véletlen hibákkal terhelt adatait simítja
    # Az mdFocus függvény első hívását követően a "tol"-ban megadott
    # értéknél nagyobb hibát tartalmazó pontokat kiveszi és az egész mérési
    # adatsort tömöríti.
    # A függvény visszatérésekor várhatóan kevesebb mérési pont lesz,
    # mint hívásakor, ezért gondoskodni kell az eredeti adatok tárolásáról.
    wx = mCopy(wX)
    wy = mCopy(wY)
    N = len(wX)
    lostPoints = []
    k = 0
    # A pontsorozat első simítása
    (av1,dt1) = mdFocus(wy,nf,S)
    if( av1==0 and dt1==0 ):
        print("HIBA")
        return
    I = 0
    tm = av1*tol
    # Az átlagosnál jobban eltérő pontok eltávolítása
    for i in range(N):
        if( abs(wy[i]-wY[i])>tm ):
            lostPoints.append([])
            lostPoints[k].append(i)
            lostPoints[k].append(wx[i])
            lostPoints[k].append(wy[i])
            k += 1
    # A megmaradt pontok tömörítése a kihagyott pontok után
    lostPoints.append([])
    lostPoints[k].append(N)
    lostPoints[k].append(0)
    lostPoints[k].append(0)
    lostN = k
    wwx = []
    wwy = []
    i0 = 0
    for i in range(lostN+1):
        for j in range(i0,lostPoints[i][0]):
            wwx.append(wx[j])
            wwy.append(wy[j])
        i0 = lostPoints[i][0]+1   
    N = len(wwy)
     # A pontsorozat második simítása az eltávolított pontok után
    (av2,dt2) = mdFocus(wy,nf,S)
    return(N,wwx,wwy,lostPoints,(av1,dt1,av2,dt2))


##################################################################################
# Objektum, mérési eredmények kiértékeléséhez egyváltozós lineáris és parametrikus
# valammint többváltozós lineáris közelítőfüggvények esetében

# Alkalmazható közelítőfüggvények
#################################
# Lineáris közelítőfüggvények

# Polinom
def FNFPol(x,y,param):
    "Polinom linarizált forma"
    r = param[1]+1
    w = DIM(r)
    fy = y
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*x
    return(w,fy)
def FNYPol(coeff,x,param):
    "Polinom értéke"
    r = len(coeff)
    w = coeff[r-1]*x
    for k in range(r-2,0,-1):
        w =x*(w+coeff[k])
    return(w+coeff[0])


# Exponenciális polinom
def FNFepol(x,y,param):
    "Exponenciális polinom linearizált forma"
    r = param[1]+1
    w = DIM(r)
    fy = log(y)
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*x
    return( w,fy)
def FNYepol(coeff,x,param):
    "Exponenciális polinom értéke"
    r = len(coeff)
    w = 0
    for k in range(r-2,0,-1):
        w = (w+coeff[k])*x
    return(exp(w+coeff[0]))
        

# Logaritmikus polinom
def FNFlpol(x,y,param):
    "Logaritmikus polinom linearizált forma"
    r = param[1]+1
    w = DIM(r)
    fx =log(x)
    fy = y
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*fx
    return(w,fy)
def FNYlpol(coeff,x,param):
    "Logaritmikus polinom értéke"
    r = len(coeff)
    fx =log(x)
    w = coeff[r-1]*fx
    for k in range(r-2,0,-1):
        w =fx*(w+coeff[k])
    return(w+coeff[0])


# Hatványfüggvény
def FNFpow(x,y,param):
    "Hatványfüggvény linearizált forma"
    r = param[1]+1
    w = DIM(r)
    fy = log(y)
    fx = log(x)
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*fx
    return(w,fy)
def FNYpow(coeff,x,param):
    "Hatványfüggvény értéke"
    r = len(coeff)
    fx =log(x)
    w = coeff[r-1]*fx
    for k in range(r-2,0,-1):
        w =fx*(w+coeff[k])
    return(exp(w+coeff[0]))


# Racionális törtfüggvény
def FNFrac(x,y,param):
    "(f,y) = FNFRac(x,y) racionális törtfüggvény linearizált forma"
    p = param[1]
    r = param[2]
    fy = y
    w = vectNULL(r+p+1)
    w[0] = 1
    for k in range(1,p+1):
        w[k] = w[k-1]*x
    w[p+1]=-fy*x
    for k in range(p+2,r+p+1):
        w[k] = w[k-1]*x
    return( w,fy )
def FNYrac(coeff,x,param):
    "(f,y) = FNYRac(coef,x): közelítőfüggvény = racionális törtfüggvény"
    r = param[1]
    p = param[2]
    wR=wP=0
    wR = coeff[r]*x
    for k in range(r-1,0,-1):
        wR =x*(wR+coeff[k])
    wR += coeff[0]
    wP = coeff[r+p]*x
    for k in range(r+p-1,r,-1):
        wP = x*(wP+coeff[k])
    return(wR/(wP+1))


# Trigonometrikus polinom
def FNFtrig(x,y,param):
    "(f,y) = FNFTrigpol(x,y) trigonometrikus polinom linearizált forma"
    p = param[1]
    r = param[2]
    fy = y
    w = vectNULL(r+p+1)
    w[0] = 1
    for k in range(1,r+1):
        w[k] = sin(k*x)
    for k in range(1,p+1):
        w[r+k] = cos(k*x)
    return( w,fy )
def FNYtrig(coeff,x,param):
    "(f,y) = FNYTrigpol(coef,x) trigonometrikus polinom értéke"
    p = param[1]
    r = param[2]
    w = coeff[0]
    for k in range(1,r+1):
        w += coeff[k]*sin(k*x)
    for k in range(1,p+1):
        w += coeff[r+k]*cos(k*x)
    return(w)

          
# Parametrikus függvények
#########################

# Parametrikus polinom
def FNFppol(x,y,param):
    "(f,y) = FNFPol(r,x,y) parametrikus polinom linearizált forma"
    # Parametrikus polinom
    r = param[1]+1
    a = param[3]
    w = vectNULL(r)
    fx = x**a
    fy = y
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*fx
    return(w,fy)
def FNYppol(p,x,param):
    "y = FNYPol(r,x) parametrikus polinom értéke "
    r = len(p)
    a = param[3]
    fx = x**a
    w = p[r-1]*fx
    for k in range(r-2,0,-1):
        w =fx*(w+p[k])
    return((w+p[0]))
def FNDppol(p,x,param):
    "dy/dx(x) = FNDPolp(r,x) parametrikus polinom derivált függvénye"
    # Parametrikus polinom
    r = len(p)
    a = param[3]
    fx = x**a
    w = 0
    for k in range(r-1,0,-1):
        w = fx*(w+k*p[k])
    return(log(x)*w)


# Parametrikus reciprokfüggvény
def FNFprec(x,y,param):
    "(f,y) = FNFRec(r,x,y) parametrikus reciprokfüggvény"
    r = param[1]+1
    a = param[3]
    fx = x**a
    fy = 1/y
    w = vectNULL(r)
    w[0] = 1
    for k in range(1,r):
        w[k] = w[k-1]*fx
    return(w,fy)
def FNYprec(p,x,param):
    " y = FNYRec(p,x,a) parametrikus reciprokfüggvény értéke"
    r = len(p)
    a = param[3]
    fx = x**a
    w = p[r-1]*fx
    for k in range(r-2,0,-1):
        w = fx*(w+p[k])
    return(1/(w+p[0]))
def FNDprec(p,x,param):
    "Parametrikus reciprokfüggvény derivált függvénye"
    r = len(p)
    a = paramm[3]
    fx = x**a
    w = 0
    for k in range(r-1,0,-1):
        w = fx*(w+k*p[k])
    w1 = p[r-1]*fx
    # a deriválthoz ki kell számítani a függvényértéket az x helyen
    for k in range(r-2,0,-1):
        w1 = fx*(w1+p[k])
    w1 = 1/(w1+p[0])
    return(log(x)*w/w1**2)


# Parametrikus trigonometrikus polinom
def FNFptrig(x,y,param):
    "Parametrikus trigonometrikus polinom"
    r = param[1]
    p = param[2]
    a = param[3]
    fy = y
    w = vectNULL(r+p+1)
    w[0] = 1
    for k in range(1,r+1):
        w[k] = sin(k*a*x)
    for k in range(1,p+1):
        w[r+k] = cos(k*a*x)
    return(w,fy)
def FNYptrig(c,x,param):
    "Parametrikus trigonometrikus polinom értéke"
    r = param[1]
    p = param[2]
    a = param[3]
    w = c[0]
    for k in range(1,r+1):
        w += c[k]*sin(k*a*x)
    for k in range(1,p+1):
        w += c[r+k]*cos(k*a*x)
    return(w)
def FNDptrig(c,x,param):
    "Prametrikus trigonometrikus polinom derivált függvénye"
    r = param[1]
    p = param[2]
    a = param[3]
    w = 0
    for k in range(1,r+1):
        w += c[k]*k*x*cos(k*a*x)
    for k in range(1,p+1):
        w -= c[r+k]*k*x*sin(k*a*x)
    return(w)


# Többváltozós függvények
#########################

# Többváltozós lineáris regresszió
def FNFmlin(wX,y,param):
    "Többváltozós lineáris regresszió linearizált forma"
    r = param[1]    # Független változók száma
    fy = y
    w = vectNULL(r+1)
    w[0]= 1
    for k in range(1,r+1):
        w[k] = wX[k-1]
    return(w,fy)
def FNYmlin(c,wX,param):
    "Többváltozós lineáris regresszió, a függvény értéke"
    r = param[1]
    w = c[0]
    for k in range(1,r+1):
        w += c[k]*wX[k-1]
    return(w)

# Többváltozós hatványfüggvény
def FNFmpow(wX,y,param):
    "Többváltozós hatványfüggvény linearizált forma"
    r = param[1]
    fy = log(y)
    w = vectNULL(r+1)
    w[0] = 1
    for k in range(1,r+1):
        w[k] = log(wX[k-1])
    return(w,fy)
def FNYmpow(c,wX,param):
    "Többváltozós hatványfüggvény értéke"
    r = param[1]
    w = exp(c[0])
    for k in range(1,r+1):
        w *= wX[k-1]**c[k]
    return(w)


# Kétváltozós polinom
def FNFbpol(wX,y,param):
    "Kétváltozós polinom linearizált forma"
    fy = y
    w = DIM(param[1]*param[2]+param[1]+param[2]+1)
    j = 0
    for k in range(param[1]+1):
        for l in range(param[2]+1):
            w[j] = wX[0]**k*wX[1]**l
            j += 1
    return(w,fy)
def FNYbpol(c,wX,a):
    "Kétváltozós polinom értéke"
    w = 0
    j = 0
    for k in range(param[1]+1):
        for l in range(param[2]+1):
            w += c[j]*wX[0]**k*wX[1]**l
            j += 1
    return(w)


# Példa egyedi közelítőfüggvény készítésére, az Antoine típusú függvény
def FNFAntoine(x,y,param):
    "Mérési adatok közelítése Antoine típusú függvénnyel"
    w = DIM(3)
    w[0] = 1
    w[1] = x
    w[2] = -x*y
    return(w,y)
def FNYAntoine(Coeff,x,param):
    return((Coeff[0]+Coeff[1]*x)/(1+Coeff[2]*x))


# A regressziós model objektum
class regrModell:
    def __init__(self,fuggveny="",valtozok=[],parameterek=[],alfa=[]):
        #Változók beállítása
        self.X = valtozok[0]
        self.Y = valtozok[1]
        self.param = DIM(6)
        self.title = ""
        # A közelítőfüggvények paramétereinek beállítása
        if( fuggveny=="pol" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.FNF = FNFPol
            self.FNY = FNYPol
            self.fN = "Polinom"
        elif( fuggveny=="epol" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.FNF = FNFepol
            self.FNY = FNYepol
            self.fN = "Exponenciális polinom"
        elif( fuggveny=="lpol" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.FNF = FNFlpol
            self.FNY = FNYlpol
            self.fN = "Logaritmikus polinom"
        elif( fuggveny=="pow" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.FNF = FNFpow
            self.FNY = FNYpow
            self.fN = "Hatványfüggvény"
        elif( fuggveny=="rac" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.param[2] = parameterek[1]
            self.FNF = FNFrac
            self.FNY = FNYrac
            self.fN = "Racionális törtfüggvény"
        elif( fuggveny=="trig" ):
            self.param[0] = "lin"
            self.param[1] = parameterek[0]
            self.param[2] = parameterek[1]
            self.FNF = FNFtrig
            self.FNY = FNYtrig
            self.fN = "Trigonometrikus polinom"
        elif( fuggveny=="ppol" ):
            self.param[0] = "par"
            self.param[1] = parameterek[0]
            self.param[3] = parameterek[2]
            self.param[4] = alfa[0]
            self.param[5] = alfa[1]
            self.FNF = FNFppol
            self.FNY = FNYppol
            self.FND = FNDppol
            self.fN = "Parametrikus polinom"
        elif( fuggveny=="prec" ):
            self.param[0] = "par"
            self.param[1] = parameterek[0]
            self.param[3] = parameterek[2]
            self.param[4] = alfa[0]
            self.param[5] = alfa[1]
            self.FNF = FNFprec
            self.FNY = FNYprec
            self.FND = FNDprec
            self.fN = "Parametrikus reciprokfüggvény"
        elif( fuggveny=="ptrig" ):
            self.param[0] = "par"
            self.param[1] = parameterek[0]
            self.param[2] = parameterek[1]
            self.param[3] = parameterek[2]
            self.param[4] = alfa[0]
            self.param[5] = alfa[1]
            self.FNF = FNFptrig
            self.FNY = FNYptrig
            self.FND = FNDptrig
            self.fN = "Parametrikus trigonometrikus polinom"
        elif( fuggveny=="mlin" ):
            self.param[0] = "mlin"
            self.param[1] = parameterek[0]
            self.FNF = FNFmlin
            self.FNY = FNYmlin
            self.fN = "Többváltozós lineáris regresszió"
        elif( fuggveny=="mpow" ):
            self.param[0] = "mlin"
            self.param[1] = parameterek[0]
            self.FNF = FNFmpow
            self.FNY = FNYmpow
            self.FND = FNDmpow
            self.fN = "Többváltozós hatványfüggvény"
        elif( fuggveny=="bpol" ):
            self.param[0] = "mlin"
            self.param[1] = parameterek[0]
            self.param[2] = parameterek[1]
            self.FNF = FNFbpol
            self.FNY = FNYbpol
            self.fN = "Kétváltozós polinom"
        elif( fuggveny=="anti" ):
            self.param[0] = "lin"
            self.param[1] = 1
            self.param[2] = 1
            self.FNF = FNFAntoine
            self.FNY = FNYAntoine
            self.fN = "Antoine függvény"
        else:
            print("GPRP: Nem létező közelítőfüggvény")
        # Model számítás, eredmények
        # Közelítőfüggvény paramétereinek számítása
        if( self.param[0]=="lin" ):
            (self.Hiba,self.Coeff,self.Corr,self.estY,self.sign) = self.GPRP()
            return
        if( self.param[0]=="par" ):
            self.param[3] = self.param[4]
            (self.Hiba,self.Coeff,self.Corr,self.estY,e1) = self.GPRP()
            self.param[3] = self.param[5]
            (self.Hiba,self.Coeff,self.Corr,self.estY,e2) = self.GPRP()
            if( e1*e2>0 ):
                print("A megadott tartomány nem megfelelő!")
                print("A findAlfa(min, max, lépés) metódus használatával lehet új paramétertartományt keresni")
                print("Ha a lépés értékét megadja, akkor a paraméter alsó és felső határia között az értékek megjelenítésre kerülnek")
                return
            self.param[3] = self.param[5]-(self.param[5]-self.param[4])/(e2-e1)*e2
            cond = abs((self.param[5]-self.param[4])/(self.param[3]+1e-10))
            while( cond>1e-3 ):
                (self.Hiba,self.Coeff,self.Corr,self.estY,e) = self.GPRP()
                if( e*e2>0 ):
                    e1 = e1/2
                else:
                    self.param[4] = self.param[5]
                    e1 = e2
                self.param[5] = self.param[3]
                e2 = e
                self.param[3] = self.param[5]-(self.param[5]-self.param[4])/(e2-e1)*e2
                cond = abs((self.param[5]-self.param[4])/(self.param[3]+1e-10))
            return
        if( self.param[0]=="mlin" ):
            (self.Hiba,self.Coeff,self.Corr,self.estY,self.sign) = self.GPRP()
            return
        
            
      
    def GPRP(self):
        "Általános regressziós keretprogram"
        # Paraméter táblázat
        # param[0]: közelítéstípus
        # param[1]: összegzés (számláló) felső határa
        # param[2]: összegzés (nevező) felső határa
        param = self.param
        # FNF együtthatókra vonatkozó függvény
        FNF = self.FNF
        # FNY közelítő függvény
        FNY = self.FNY
        # FND közelítőfüggvény deriváltja
        if( param[0] == "par" ):
            FND = self.FND
        # paraméteres esetben a=paraméter aktuális értéke
        a = param[3]
        X = self.X
        Y = self.Y
        N = len(X)
        r = int(param[1]+param[2]+1)
        if( FNF==FNFbpol ):
            r = param[4]*param[5]+param[4]+param[5]+1
        wB = DIM(r,r)
        wA = DIM(r)
        wF = DIM(r)
        for i in range(N):
            y = Y[i]
            (f,y) = FNF(X[i],Y[i],param)
            for k in range(r):
                for l in range(k,r):
                    wB[k][l]+=f[k]*f[l]
                    wB[l][k]=wB[k][l]
            wf = vectScal(y,f)
            wA = vectAdd(wA,wf)
        p = matrGauss(wB,wA)
        if( sum(p)==0 ):
            return("Nincs megoldás",[],[],0,0)
        err = "OK"
        w0 = 0
        if( param[0]=="par" ):
            # A FI(alfa) értékének számítása
            for i in range(N):
                w0 += (FNY(p,X[i],param)-Y[i])*FND(p,X[i],param)
        wcy = []   
        for i in range(N):
            wcy.append(FNY(p,X[i],param))
        cr = mdCorrcoeff(Y,wcy)
        return(err,p,cr,wcy,w0)
    

    def Print(self,Title="",rp="n"):
        "Eredmények nyomtatása"
        # param[0]: a közelítés típusa ("lin","par",mLin")
        # param[1]: fokszám 1
        # param[2]: fokszám 2
        # param[3]: paraméter (alfa)
        # CY: x értékek, y értékek, közelített értékek
        # Azonosító feliratok
        self.title = Title
        # Az adatok és eredmények megjelenítésének pontossága
        precData = "13.4f"
        precCoef = "7.4f"
        prd = '%'+precData+'\t\t%'+precData+'\t\t%'+precData+'\t\t%'+precData
        #A pillanatnyi dátum és idő lekérése és formázása
        ido = datetime.now()
        ido = ido.strftime("%Y-%m-%d %H:%M%S")
        #tdt = f"{datetime.today():%Y-%B-%d  %H:%M}"
        print(Title)
        if( self.param[0]=="lin" or self.param[0]=="mlin" ):
            print("Közelítés típusa: lineáris")
        else:
            print("Közelítés típusa: parametrikus")
        print("Közelítőfüggvény:",self.fN)
        if( self.param[0]!="mlin" ):
            print("Fokszám:\nr=",self.param[1],"\np=",self.param[2])
            print("Együtthatók:")
            mPrint(self.Coeff,precCoef)
            if( self.param[0]=="par" ):
                print("Paraméter:%7.4f" %self.param[3])
            print('\nKorrelációs együttható:%6.4f\n' %self.Corr)
            # A közelített értékek nyomtatása, ha kell
            if( rp!="n" ):
                print("         X            Y            cY         deltaY ")
                for i in range(len(self.estY)):
                    prs = format(self.X[i],precData)
                    prs += format(self.Y[i],precData)
                    prs += format(self.estY[i],precData)
                    prs += format(abs(self.Y[i]-self.estY[i]),precData)
                    print(prs)
            return
        #Többdimenziós közelítés eredményének nyomtatása
        print("Dimenziók száma:",self.param[1])
        print("Együtthatók:")
        if( self.fN=="mpow" ):
            self.Coeff[0] = exp(self.Coef[0])
            mPrint(self.Coeff,precCoeff)
        else:
            mPrint(self.Coeff,precCoef)
        print('\nKorrelációs együttható:%6.4f\n' %self.Corr)
        return


    def Save(self,fileName="",title=""):
        "Eredmények mentése"
        if( len(fileName)==0 ):
            print("GPRP: Nincs fájlnév megadva")
            return
        precData = "13.4f"
        precCoef = "7.4f"
        f = open(fileName,'w')
        #A pillanatnyi dátum és idő lekérése és formázása
        ido = datetime.now()
        ido = ido.strftime("%Y-%m-%d %H:%M%S")
        #tdt = f"{datetime.today():%Y-%B-%d  %H:%M}"
        f.write("Mérési adatok közelítése a legkisebb négyzetek módszerével   "+ido+"\n\n")
        if( len(self.title)==0 ):
            self.title = " "
        f.write(self.title+"\n")
        f.write("Közelítőfüggvény:"+self.fN)
        f.write("\nFokszám:\nr="+str(self.param[1])+"\np="+str(self.param[2]))
        f.write("\nEgyütthatók:")
        for i in range(len(self.Coeff)):
            f.write("\n"+format(self.Coeff[i],precCoef))
        if( self.param[0]=="par" ):
            f.write("\nParaméter:"+format(self.param[3],precCoef))
        f.write("\nKorrelációs együttható:"+format(self.Corr,"6.4f"))
        f.write("\n\n")
        f.write("        X           Y           cY       deltaY \n")
        for i in range(len(self.X)):
            prs = format(self.X[i],precData)
            prs += format(self.Y[i],precData)
            prs += format(self.estY[i],precData)
            prs += format(abs(self.Y[i]-self.estY[i]),precData)
            f.write(prs+"\n")
        return


    def Plot(self,xlimits,ylimits,origo,scale,afrm=["",""],fileName=""):
        "Az eredeti mérési pontok és a közelített értékek felrajzolása"
        subtitles = ("Közelítés a legkisebb négyzetek módszerével",self.title)
        size = (1024,768)
        self.axes = Axes(size,subtitles,xlimits,ylimits,origo,scale,afrm)
        dPlot(self.axes,self.X,self.Y)
        x = xlimits[0]
        dx = (xlimits[1]-xlimits[0])/500
        wx = []
        wy = []
        while( x<=xlimits[1] ):
            wx.append(x)
            wy.append(self.FNY(self.Coeff,x,self.param))
            x += dx
        dPlot(self.axes,wx,wy,plotType="line",color="blue")
        if( len(fileName)!=0 ):
            self.axes[0].update()
            self.axes[0].postscript(file=fileName+".ps", colormode='color')  
        return


    def findAlfa(self,amin,amax,step=0,pr=1,pl=0):
        "Parametrikus függvények alfa paraméterének keresése"
        #pr = 1 Az alfa értékek nyomtatódna
        #pr = 0 Az alfa értékek NEM nyomtatódnak
        #pl = 1 Az alfa értékek felrajzolásra kerülnek
        #pl = 0 # Az alfa értékek nem kerülnek felrajzolásra
        self.param[4] = amin
        self.param[5] = amax
        self.param[3] = amin
        (self.Hiba,self.Coeff,self.Corr,self.estY,sign) = self.GPRP()
        e1 = sign
        self.param[3] = amax
        (self.Hiba,self.Coeff,self.Corr,self.estY,sign) = self.GPRP()
        e2 = sign
        if( e1*e2>0 ):
            print("A megadott paramétertartomány nem megfelelő a modell felállításához!")
            print("par(1)=%7.3f\te(1)=%7.3f\tcr=%6.4f" %(amin,e1,self.Corr))
            print("par(2)=%7.3f\te(1)=%7.3f\tcr=%6.4f" %(amax,e2,self.Corr))
        else:
            print("A megadott paramétertartomány megfelelő a modell felállításához")
        if( step!=0 ):
            wA = []
            wS = []
            self.param[3] = amin
            while(self.param[3]<amax):
                (self.Hiba,self.Coeff,self.Corr,self.estY,sign) = self.GPRP()
                if( pr!=0 ):
                    print("%7.4f\t%7.4f\t%6.4f" %(self.param[3],sign,self.Corr))
                wS.append(sign)
                wA.append(self.param[3])
                self.param[3] += step
        print(len(wA),len(wS))
        minwS = min(wS)
        maxwS = max(wS)
        stpwS = (maxwS-minwS)/10
        stpwA = (amax-amin)/10
        if( pl!=0 ):
            print("y-min:",format(minwS,"10.4f"))
            print("y-max:",format(maxwS,"10.4f"))
            print("x-tengely lépésköz:",format(stpwA,"5.2f"))
            print("y-tengely lépésköz:",format(stpwS,"5.2f"))
            rajz = Axes((1024,768),("Paraméter vizsgálata","Paraméter vizsgálata"),(amin,amax),(minwS,maxwS),(amin,0),(stpwA,stpwS))
            dPlot(rajz,wA,wS,"line","red")
        return

    def exportPlot(self,fileName,colorMode="color"):
        "Rajz exportálása postscript formátumban"
        self.axes[0].update()
        self.axes[0].postscript(file=fileName+".ps", colormode='color')
        return
        

# Az általánoscélú Regressziós Modell Vége
##########################################


# Interpoláció
##############

def interpolLagrange(x,N,wX,wY):
    "Lagrange interpoláció"
    n = len(wX)
    #  Az x tartományba esésének vizsgálata
    if( x<wX[0] ):
        return(wY[0])
    if( x>=wX[n-N-1] ):
        return(wY[n-N-1])
    L = DIM(N+1,1,1)
    i = 0
    # A megfelelő intervallum megkeresése
    while( x>wX[i] ):
        i += 1
    # Interpoláció
    if( x==wX[i] ):
        return(wY[i])
    i -= floor(N/2)
    y = 0
    for k in range(N+1):
        for j in range(N+1):
            if( j!=k ):
                L[k] = L[k]*(x-wX[i+j])/(wX[i+k]-wX[j+i])
        y += L[k]*wY[i+k]
    return(y)
    

def interpolNewton(x,N,wX,wY):
    "Harmadfokú Newton interpoláció"
    n = len(wX)
    dy = DIM(N+1,n)
    c = DIM(N)
    # Az x tartományba esésének vizsgálata
    if( x<wX[0] ):
        return(wY[0])
    if( x>wX[n-N] ):
        return(wY[n-3])
    # Differenciák kiszámítása
    for i in range(n):
        dy[0][i] = wY[i]
    for k in range(1,N+1):
        for i in range(n-k):
            dy[k][i] = (dy[k-1][i+1]-dy[k-1][i])/(wX[i+1]-wX[i])
    # Interpoláció
    i = 0
    while( x>wX[i] ):
        i += 1
    i -= 1
    c[0] = x-wX[i]
    for k in range(1,N):
        c[k] = c[k-1]*(x-wX[i+k])
    y = wY[i]
    for k in range(N):
        y += c[k]*dy[k+1][i]
    return(y)


def interpolAkima(x,wX,wY):
    "Akima szemi-Spline interpoláció"
    n = len(wX)
    wM = DIM(n+4)
    wZ = DIM(n+1)
    if( x<wX[0] ):
        return(wY[0])
    if( x>wX[n-3] ):
        return(wY[n-3])
    for i in range(n-1):
        wM[i+2] = (wY[i+1]-wY[i])/(wX[i+1]-wX[i])
    wM[1]   = 2*wM[2]-wM[3]
    wM[0]   = 2*wM[1]-wM[2]
    wM[n+2] = 2*wM[n+1]-wM[n]
    wM[n+3] = 2*wM[n+2]-wM[n+1]
    for i in range(n):
        a = abs(wM[i+3]-wM[i+2])
        b = abs(wM[i+1]-wM[i])
        if( (a+b)==0 ):
            wZ[i] = (wM[i+2]+wM[i+1])/2
        else:
            wZ[i] = (a*wM[i+1]+b*wM[i+2])/(a+b)
    k = 0
    while( x>wX[k] ):
        k += 1
    k -= 1
    b = wX[k+1]-wX[k]
    a = x-wX[k]
    y = wY[k]+wZ[k]*a
    y += (3*wM[k+2]-2*wZ[k]-wZ[k+1])*a*a/b
    y += (wZ[k]+wZ[k+1]-2*wM[k+2])*a**3/b/b
    return(y)


# Numerikus deriválás
#####################

def difFunc(x,FNF,h=1e-2,eps=1e-6):
    "Kifejezéssel adott függvény adott pontban vett differenciálhányadosának közelítése"
    
    d1 = 1
    d2 = 2
    while( abs(d1-d2)>=eps ):
        x1 = x-h
        x2 = x+h
        d2 = d1
        d1 = (FNF(x2)-FNF(x1))/(x2-x1)
        h /= 2
    return(d1)


def difTable(x,wX,wY,N=3):
    "Pontonként adott függvény adott pontban vett differenciálhányadosának közelítése"
    n = len(wX)
    #  Az x tartományba esésének vizsgálata
    if( x<wX[0] ):
        return(wY[0])
    if( x>=wX[n-N-1] ):
        return(wY[n-N-1])
    wL = DIM(N+1,1,0)
    wM = DIM(N+1,N+1,1)
    i = 0
    # A megfelelő intervallum megkeresése
    while( x>wX[i] ):
        i += 1
    # Interpoláció
    i = i-floor(N/2)
    y = 0
    for k in range(N+1):
        for j in range(N+1):
            if( j!=k ):
                for l in range(N+1):
                    if( l!=k ):
                        if( l==j ):
                            wM[l][k] = wM[l][k]/(wX[i+k]-wX[i+j])
                        if( l!=j ):
                            wM[l][k] = wM[l][k]*(x-wX[j+i])/(wX[i+k]-wX[i+j])           
        for l in range(N+1):
            if( l!=k ):
                wL[k] = wL[k]+wM[l][k]
        y = y+wL[k]*wY[i+k]
    return(y)


# Numerikus integrálás
######################

def integrTrap(a,b,n,FNF):
    "Határozott integrál számítása trapéz módszerrel"
    h = (b-a)/n
    x = a+h
    S = 0
    for i in range(n-1):
        S += FNF(x)
        x += h
    return(h/2*(FNF(a)+2*S+FNF(b)))


def integrSimps(a,b,n,FNF):
    "Határozott integrál számítása Simpson módszerrel"
    h = (b-a)/n
    x = a+h/2
    S1 = 0
    for i in range(n):
        S1 += FNF(x)
        x += h
    S2 = 0
    x = a+h
    for i in range(n-1):
        S2 += FNF(x)
        x += h
    return(h/6*((FNF(a)+FNF(b))+2*S2+4*S1))


def integrTR(a,b,wX,wY):
    "Pontsorozattal adott függvény integrálása trapéz módszerrel és lineáris interpolációval"
    # A köztes osztópontokban a függvényérték számítása lineáris interpolációval történik
    # Az integrál értékének számításában felhasználásra került a Richardson extrapoláció
    n = len(wX)
    if( a<wX[0] ):
        print("Az alsó határ kisebb mint X[0]!")
        return(-10000)
    if( b>wX[n-1] ):
        print("A felső határ nagyobb mint X[n]")
        return(-10000)
    i = 0
    while( wX[i]<=a ):
        i += 1
    i0 = i
    ya = (a-wX[i0-1])*(wY[i0]-wY[i0-1])/(wX[i0]-wX[i0-1])+wY[i0-1]
    while( wX[i]<=b ):
        i += 1
    yb = (b-wX[i-1])*(wY[i]-wY[i-1])/(wX[i]-wX[i-1])+wY[i-1]
    iin = i
    Sa = (wX[i0]-a)*(wY[i0]+ya)/2
    Sb = (wX[iin]-b)*(wY[iin]+yb)/2
    S  = 0
    S21 = 0
    S22 = 0
    for i in range(i0,iin-1,1):
        h = wX[i+1]-wX[i]
        h2 = h/2
        S += h*(wY[i]+wY[i+1])/2
        xk = wX[i]+h2
        yk = wY[i]+h2*(wY[i+1]-wY[i])/(wX[i+1]-wX[i])
        S21 += h2*(wY[i]+yk)/2
        S22 += h2*(yk+wY[i+1])/2
    return( Sa+Sb+(4*(S21+S22)-S)/3 )


def integrTRL(a,b,wX,wY):
    "Pontsorozattal adott függvény integrálása trapéz módszerrel és Lagrange interpolációval"
    # A köztes osztópontokban a függvényérték számítása Lagrange interpolációval történik
    # Az integrál értékének számításában felhasználásra került a Richardson extrapoláció
    n = len(wX)
    if( a<wX[0] ):
        return(-10000)
    if( b>wX[n-1] ):
        return(-10000)
    i = 0
    while( wX[i]<=a ):
        i += 1
    i0 = i
    ya = (a-wX[i0-1])*(wY[i0]-wY[i0-1])/(wX[i0]-wX[i0-1])+wY[i0-1]
    while( wX[i]<=b ):
        i += 1
    yb = (b-wX[i-1])*(wY[i]-wY[i-1])/(wX[i]-wX[i-1])+wY[i-1]
    iin = i
    Sa = (wX[i0]-a)*(wY[i0]+ya)/2
    Sb = (wX[iin]-b)*(wY[iin]+yb)/2
    S  = 0
    S21 = 0
    S22 = 0
    nS2 =0
    for i in range(i0,iin-1,1):
        h = wX[i+1]-wX[i]
        h2 = h/2
        S += h*(wY[i]+wY[i+1])/2
        xk = wX[i]+h2
        # y[k] számítása Lagrange interpolációval
        yk = 0
        for j1 in range(4):
            t = 1
            for j2 in range(4):
                if( j1!=j2):
                    t = t*(xk-wX[i+j2])/(wX[i+j1]-wX[i+j2])
            yk = yk+t*wY[i+j1]
        # Megvan yk
        S21 += h2*(wY[i]+yk)/2
        S22 += h2*(yk+wY[i+1])/2
        nS2 += 1
    return( Sa+Sb+(4*(S21+S22)-S)/3 )


def integrTAK(a,b,wX,wY):
    "Pontsorozattal adott függvény integrálása trapéz módszerrel és Akima interpolációval"
    # A köztes osztópontokban a függvényérték közelítése Akima interpolációval történik
    # Az integrál értékének számításában felhasználásra került a Richardson extrapoláció
    n = len(wX)
    wx = DIM(4)
    wy = DIM(4)
    if( a<wX[0] ):
        print("Az alsó határ kisebb mint X[0]!")
        return(None)
    if( b>wX[n-1] ):
        print("A felső határ nagyobb mint X[n]")
        return(None)
    i = 0
    while( wX[i]<=a ):
        i += 1
    i0 = i
    # Az a-t megelőző alappont az i0-1., a követő az i0.
    # ya és a következő alappont felezőhöz tartozó függvényérték
    # számítása Akima interpolációval
    for j1 in range(4):
        wx[j1] = wX[i0-1+j1]
        wy[j1] = wY[i0-1+j1]
    ya = interpolAkima(a,wx,wy)
    S = (wX[i0]-a)*(wY[i0]+ya)/2
    h2 = (wX[i0]-a)/2
    xk = a+h2
    yk = interpolAkima(xk,wx,wy)
    S2 = h2*(ya+yk)/2
    S2 += h2*(yk+wY[i0])/2
    while( wX[i]<=b ):
        i += 1
    # A b-t követő alappont az i., a b-t megelőző alappont i-1.
    # yb és a megelőző alappont felezőhöz tartozó függvényérték
    # számítása Akima interpolációval
    for j1 in range(4):
        wx[j1] = wX[i-1+j1]
        wy[j1] = wY[i-1+j1]
    yb = interpolAkima(b,wx,wy)
    S += (wX[i-1]-b)*(yb+wY[i-1])/2
    h2 = (b-wX[i-1])/2
    xk = b-h2
    yk =interpolAkima(xk,wx,wy)
    S2 += h2*(wY[i-1]-yk)/2
    S2 +=  h2*(yk+yb)/2
    iin = i
    nS2 =0
    for i in range(i0,iin-1,1):
        h = wX[i+1]-wX[i]
        h2 = h/2
        S += h*(wY[i]+wY[i+1])/2
        xk = wX[i]+h2
        # y[k] számítása Akima interpolációval
        for j1 in range(4):
            wx[j1] = wX[i+j1]
            wy[j1] = wY[i+j1]
        yk = interpolAkima(xk,wx,wy)
        # Megvan yk
        S2 += h2*(wY[i]+yk)/2
        S2 += h2*(yk+wY[i+1])/2
    return( (4*S2-S)/3 )


# Polinom műveletek, nemlineáris egyenletek numerikus megoldása
###############################################################
def polyAdd(p,q,op="add"):
    "Polinomok összeadása vagy kivonása"
    np = len(p)
    nq = len(q)
    if( np==0 or nq==0 ):
        return(0)
    c = 1
    if( op=="sub" ):
        c = -1
    a = 0
    minr = min(np,nq)
    maxr = max(np,nq)
    r = DIM(maxr)
    for i in range(np):
        r[i] = p[i]
    for i in range(nq):
        r[i] = r[i]+c*q[i]
    return(r)
    
 
def polyMult(p,q):
    "Polinomok szorzása"
    np = len(p)
    nq = len(q)
    nr = np+nq-1
    r = DIM(nr)
    for i in range(np):
        for j in range(nq):
            k = i+j-1
            r[k] += p[i]*q[j]
    r = vectShift(r)
    return(r)
        

def polyDiv(p,q):
    "Polinomok osztása"
    nx = len(p)
    ny = len(q)
    if( ny>nx ):
        print("Az osztó fokszáma nagyobb mint az osztandó fokszáma")
        return(0,0)
    wx = mCopy(p)
    wy = mCopy(q) 
    nz = nx-ny+1
    wz = DIM(nz)
    eps = 1e-8
    ix = ny-1
    i = nz
    while( i>0 ):
        ii = i+ix
        wz[i-1] = wx[ii-1]/wy[ny-1]
        for k in range(0,ix):
            j = k-1+i
            wx[j] = wx[j]-wz[i-1]*wy[k]
        i -= 1
    return(wz,wx[0:nx-nz])


def polyInfo(p):
    "Információ polinom valós gyökeiről"
    wx = mCopy(p)
    nx = len(wx)
    print("Információ a ",wx," polinom valós gyökeiről")
    print("Gyökök száma:",nx-1)
    for i in range(nx):
        wx[i] = wx[i]/wx[nx-1]
    maxRoot = wx[nx-2]*wx[nx-2]-2*wx[nx-3]
    if( maxRoot>0 ):
        maxRoot = sqrt(maxRoot)
        print("A legnagyobb gyök kisebb vagy egyenlő mint:",maxRoot)
    else:
        maxRoot = 0
        print("A polinomnak legalább két komplex gyöke van")
        return
    if( floor((nx-1)/2)==(nx-1)/2 ):
        a = wx[0]
    else:
        a = -wx[0]
    if( a<=0 ):
        z1 = 1
        print("Legalább egy negatív valós gyök van")
    else:
        z1 = 0
    z2 = 0
    for i in range(1,nx):
        if( wx[i]*wx[i-1]<0 ):
            z2 += 1
    if( z2>=1 ):
        print("Legfeljebb" ,z2," pozitív valós gyök van")
    z3 = 0
    for i in range(1,nx):
        if( wx[i]*wx[i-1]>0 ):
            z3 += 1
    if( z3>=1 ):
        print("Legfeljebb ",z3," negatív valós gyök van")
    if( floor(z2/2)!=z2/2 ):
        print("Van legalább egy pozitív valós gyök")
    if( (floor(z3/2)!= z3/2) and (z1!=1) ):
        print("Legalább egy negatív gyök van")
    return


def rootSearch(FNF,a,b,N):
    "Gyököket tartalmazó intervallumok keresése"
    wX = setList(a,b,(b-a)/N)
    wY = evalPFunc(wX,FNF,[])
    wR = []
    j = 0
    for i in range(N-2):
        if( wY[i]*wY[i+1]<=0 ):
            wR.append([])
            wR[j].append(wX[i])
            wR[j].append(wX[i+1])
            j += 1
    return(wR)
   

def rootBisect(FNF,x0,x,eps=1e-6,NMAX=1000):
    "Valós egyváltozós nemlineáris egyenlet gyökének közelítése intervallumfelezés módszerrel"
    N = 0
    y = FNF(x)
    y0 = FNF(x0)
    if( (y0*y)>0 ):
        print("Nem jó intervallum!")
        return(0)
    while( abs(x0-x)>eps ):
        xr = x
        yr = y
        x = (x0+x)/2
        y = FNF(x)
        if( yr*y<0 ):
            x0 = x
            y0 = y
            x = xr
            y = yr
        N += 1
        if( N>NMAX ):
            # Kiírjuk a képernyőre az iterációk számát
            print("Az iteráció lépésszáma elérte a megadott korlátot!")
            return(x)
    print(N)
    return(x)
        

def rootSecant(FNF,x0,x1,eps=1e-6,NMAX=1000):
    "Valós egyváltozós nemlineáris egyenlet gyökének közelítése érintő módszerrel"
    N = 0
    y0 = FNF(x0)
    y1 = FNF(x1)
    while( abs(x0-x1)>eps ):
        if( y0==y1 ):
            y1 += 0.0001
        x = (x0*y1-y0*x1)/(y1-y0)
        x0 = x1
        y0 = y1
        x1 = x
        y1 = FNF(x)
        N += 1
        if( N>NMAX ):
            # Kiírjuk a képernyőre az iterációk számát
            print("Az iteráció lépésszáma elérte a megadott korlátot!")
            return(x1)
    print(N)
    return(x1)


def rootRegula(FNF,x0,x1,eps=1e-6,NMAX=1000):
    "Valós egyváltozós nemlineáris egyenlet gyökének közelítése 'regula falsi' módszerrel"
    N = 0
    if( x0<x1 ):
        y0 = FNF(x0)
        y1 = FNF(x1)
    else:
        x = x1
        y0 = FNF(x)
        x1 = x0
        x0 = x
        y1 = FNF(x1)
    xr = x0
    x = x1
    while( abs(xr-x)>eps ):
        xr = x
        x = (x0*y1-y0*x1)/(y1-y0)
        y = FNF(x)
        if( y0*y<0 ):
            x1 = x
            y1 = y
        if( y1*y<0 ):
            x0 = x
            y0 = y
        N += 1
        if( N>NMAX ):
            # Kiírjuk a képernyőre az iterációk számát
            print("Az iteráció lépésszáma elérte a megadott korlátot!")
            return(x)
    print(N)
    return(x)


def rootNewton(FNF,FND,x0,eps=1e-6,NMAX=1000):
    "Valós egyváltozós nemlineáris egyenlet gyökének közelítése Newton módszerrel"
    N = 0
    x = x0-FNF(x0)/FND(x0)
    while( abs(x-x0)>eps ):
        N += 1
        x0 = x
        x = x0-FNF(x0)/FND(x0)
        if( N>NMAX ):
            print("Az iteráció lépésszáma elérte a megadott korlátot!")
            return(x)   
    # Kiírjuk a képernyőre az iterációk számát
    print(N)
    return(x)
    
 
def rootAitken(FNF,x0,eps=1e-6,NMAX=1000):
    "Valós, egyváltozós nemlineáris egyenlet gyökének közelítése Aitken iterációval"
    x1 = FNF(x0)
    x2 = FNF(x1)
    N = 2
    if( x2-2*x1+x0==0 ):
            x0 += 0.0001
    a = (x1-x0)**2/(x2-2*x1+x0)
    while( abs(x0-x1)>eps ):
        if( x2-2*x1+x0==0 ):
            x0 += 0.0001
        a = (x1-x0)**2/(x2-2*x1+x0)
        x0 = x0-a
        x1 = FNF(x0)
        x2 = FNF(x1)
        N += 1
        if( N>NMAX ):
            print(N)
            return(x0)
    print(N)
    return(x0)
    
                        
# Közönséges differenciálegyenletek megoldása
#############################################
def diffEuler(FNF,y0,a,b,N):
    "Közönséges differenciálegyenlet megoldása explicit Euler módszerrel"
    h = (b-a)/N
    t = DIM(N+1)
    y = DIM(N+1)
    y[0] = y0
    for n in range(1,N+1):
        t[n] = t[n-1]+h
        y[n] = y[n-1]+h*FNF(t[n-1],y[n-1])
    return(h,t,y)


def diffRungeKutta(FNF,y0,a,b,N,method="RK4"):
    "Közönséges differenciálegyenletek megoldása Runge-Kutta módszerrel"
    #method: EUL  -> javított Euler módszer
    #method: RK2  -> másodrendű RK módszer
    #method: RK3  -> harmadrendű RK (Heun) módszer
    #method: RK4  -> Kutta negyedrendű módszere
    h = (b-a)/N
    t = setList(a,b,h)
    tN = len(t)
    y = DIM(tN)
    y[0] = y0
    if( method=="EUL" ):
        for n in range(1,tN):
            k1 = FNF(t[n-1],y[n-1])
            y[n] = y[n-1]+0.5*h*(k1+FNF(t[n],y[n-1]+h*k1))
        return(h,t,y)
    if( method=="RK2" ):
        for n in range(1,tN):
            k1 = FNF(t[n-1],y[n-1])
            k2 = 0.5*k1
            y[n] = y[n-1]+h*FNF(t[n-1]+0.5*h,y[n-1]+h*k2)
        return(h,t,y)
    if( method=="RK3" ):
        for n in range(1,tN):
            k1 = FNF(t[n-1],y[n-1])
            k2 = FNF(t[n-1]+h/3,y[n-1]+2/3*h*k1)
            k3 = FNF(t[n-1]+2/3*h,y[n-1]+2/3*h*k2)
            y[n] = y[n-1]+0.25*h*k1+0.75*h*k3            
        return(h,t,y)
    if( method=="RK4" ):
        for n in range(1,tN):
            k1 = FNF(t[n-1],y[n-1])
            k2 = FNF(t[n-1]+0.5*h,y[n-1]+0.5*h*k1)
            k3 = FNF(t[n-1]+0.5*h,y[n-1]+0.5*h*k2)
            k4 = FNF(t[n-1]+h,y[n-1]+h*k3)
            y[n] = y[n-1]+h*(k1/6+k2/3+k3/3+k4/6)
        return(h,t,y)
    print("Hibás módszer megnevezés")
    return(h,t,y)


def diffAB(FNF,y0,a,b,N,eps=1e-4):
    "Közönséges differenciálegyenlet megoldása Adams-Bashforth prediktor-korrektor módszerrel"
    h = (b-a)/N
    t = DIM(N+1)
    y = DIM(N+1)
    # Az első két szükséges érték meghatározása RK4 módszerrel
    [h1,t1,y1] = diffRungeKutta(FNF,y0,a,a+2*h,2)
    # A prediktor-korrektor módszer, az iteráció elindításához szükséges értékek
    t[0] = Tn_2 = t1[0]
    t[1] = Tn_1 = t1[1]
    t[2] = Tn   = t1[2]
    y[0] = Yn_2 = y1[0]
    y[1] = Yn_1 = y1[1]
    y[2] = Yn   = y1[2]
    # Az AB módszer indítása a teljes intervallumra
    for n in range(3,N+1):
        Tn1 = t[n] = Tn+h
        # Prediktor
        k1 = FNF(Tn,Yn)
        Y0 = Yn_2+1.5*h*(k1-FNF(Tn_1,Yn-1))
        d = 100
        # Korrektor iteráció
        while( d>= eps ):
            Y1 = Yn+0.5*h*(FNF(Tn1,Y0)+k1)
            d = abs(Y1-Y0)
            Y0 = Y1
        # Korrektor iterációjának vége
        y[n] = Y1
        Tn_2 = Tn_1
        Yn_2 = Yn_1
        Tn_1 = Tn
        Yn_1 = Yn
        Tn   = Tn1
        Yn   = Y1
        # Vége az intervallumon belüli ciklusnak
    return(h,t,y)
    

def diffAdamsBashforth(FNF,y0,a0,b0,N,K=4):
    "Explicit Adam-Bashforth módszer"
    # Adams-Bashforth együtthatók
    a = DIM(5,5)
    a[1][1] =1
    a[2][1] =-1/2
    a[2][2] = 3/2
    a[3][1] = 15/12
    a[3][2] = -16/12
    a[3][3] = 23/12
    a[4][1] = -9/24
    a[4][2] = 37/24
    a[4][3] = -59/24
    a[4][4] = 55/24
    ####
    Yi = DIM(5)
    t = DIM(N+1)
    y = DIM(N+1)
    h = (b0-a0)/N
    ####
    # Kezdeti értékek kiszámítása 4-ed rendű Runge-Kutta módszerrel
    for i in range(1,K+1):
        [h1,t1,y1] = diffRungeKutta(FNF,y0,a0,a0+K*h,K)
    for i in range(1,K+1):
        y[i] = y1[i]
        t[i] = t1[i]
    # Intervallumonkénti ciklus
    for n in range(K,N+1):
        t[n] = t[n-1]+h
        # K szerinti ciklusban az y(n+1) számítása
        Yn1 = y[n-1]
        for k in range(1,K+1):
            Yn1 = Yn1+h*a[K][k]*FNF(t[n-K+k-1],y[n-K+k-1])
        print(n,Yn1)
        y[n] = Yn1
    # Vége az intervallumonkénti ciklusnak
    return(h,t,y)


def diffMilneHamming(FNF,y0,a0,b0,N,eps=1e-4):
    "Milne-Hamming prediktor-korrektor módszer"
    Yi = DIM(4)
    t = DIM(N+1)
    y = DIM(N+1)
    h = (b0-a0)/N
    # Kezdeti értékek kiszámítása 4-ed rendű Runge-Kutta módszerrel
    for i in range(1,4):
        [h1,Ti,Yi] = diffRungeKutta(FNF,y0,a0,a0+3*h,3)
    for i in range(0,4):
        y[i] = Yi[i]
        t[i] = Ti[i]
    # A 3. pontban a Milne prediktorával kapott érték, pontosat teszünk bele
    Yn0 = y[3]
    # Intervallumonkénti ciklus
    for n in range(4,N+1):
        t[n] = t[n-1]+h
        # y[n) kezdeti értékének számítása Milne prediktorával
        Y0 = y[n-4]+4/3*h*(2*FNF(t[n-1],y[n-1])-FNF(t[n-2],y[n-2])+2*FNF(t[n-3],y[n-3]))
        # kezdeti érték javítása
        Y0 = Y0+112/121*(FNF(t[n-1],y[n-1])-FNF(t[n-1],Yn0))
        Yn0 = Y0
        # Iteráció a korrektorral
        d = 100
        while( d>eps ):
            Y1 = 1/8*(9*y[n-1]-y[n-3])
            Y1 = Y1+3/8*h*(FNF(t[n],Y0)+2*FNF(t[n-1],y[n-1])-FNF(t[n-1],y[n-2]))
            d = abs(Y0-Y1)
            Y0 = Y1
            # Korrektor iteráció vége
        y[n] = Y1
    # Intervallumonkénti ciklus vége
    return(h,t,y)


def diffERungeKutta(FNF,Y0,a,b,N,method="RK4"):
    "Elsőrendű differenciálegyenlet rendszerek megoldása Runge-Kutta módszerrel"
    #method: EUL  -> javított Euler módszer
    #method: RK2  -> másodrendű RK módszer
    #method: RK3  -> harmadrendű RK (Heun) módszer
    #method: RK4  -> Kutta negyedrendű módszere
    M = len(Y0) # Egyenletek száma
    h = (b-a)/N
    t = setList(a,b,h)
    Y = DIM(M,N+1)
    for i in range(M):
        Y[i][0] = Y0[i]
    if( method=="EUL" ):
        K1 = DIM(M)
        Y1 = DIM(M)
        Y2 = DIM(M)
        Y3 = DIM(M)
        for n in range(1,N+1):
            Y1 = mdCol(Y,n-1)
            K1 = FNF(t[n-1],Y1)
            Y2 = mAdd(Y1,mScal(h,K1))
            Y3 = FNF(t,Y2)
            Y3 = mAdd(Y1,vectScal(0.5*h,mAdd(K1,Y3)))
            vectMove(Y3,Y,n)
        return(h,t,Y)
    if( method=="RK2" ):
        K1 = DIM(M)
        K2 = DIM(M)
        Y1 = DIM(M)
        Y2 = DIM(M)
        for n in range(1,N+1):
            Y1 = mdCol(Y,n-1)
            K1 = FNF(t[n-1],Y1)
            K2 = vectScal(0.5,K1)
            Y3 = FNF(t[n-1]+0.5*h,mAdd(Y1,mScal(h,K2)))
            Y3 = mAdd(Y1,vectScal(h,Y3))
            vectMove(Y3,Y,n)
        return(h,t,Y)
    if( method=="RK3" ):
        K1 = DIM(M)
        K2 = DIM(M)
        K3 = DIM(M)
        Y1 = DIM(M)
        Y2 = DIM(M)
        for n in range(1,N+1):
            Y1 = mdCol(Y,n-1)
            K1 = FNF(t[n-1],Y1)
            K2 = FNF(t[n-1]+h,mAdd(Y1,mScal(2/3*h,K1)))
            K3 = FNF(t[n-1]+2/3*h,mAdd(Y1,mScal(2/3*h,K2)))
            Y2 = mAdd(Y1,mScal(0.25*h,K1))
            Y2 = mAdd(Y2,mScal(0.75*h,K3))
            vectMove(Y2,Y,n)   
        return(h,t,Y)
    if( method=="RK4" ):
        K1 = DIM(M)
        K2 = DIM(M)
        K3 = DIM(M)
        K4 = DIM(M)
        Y1 = DIM(M)
        Y2 = DIM(M)
        for n in range(1,N+1):
            Y1 = mdCol(Y,n-1)
            K1 = FNF(t[n-1],Y1)
            K2 = FNF(t[n-1]*h,mAdd(Y1,mScal(0.5*h,K1)))
            K3 = FNF(t[n-1]+0.5*h,mAdd(Y1,mScal(0.5*h,K2)))
            K4 = FNF(t[n-1]+h,mAdd(Y1,mScal(h,K3)))
            Y2 = mAdd(mScal(1/6,K1),mScal(1/3,K2))
            Y2 = mAdd(Y2,mScal(1/3,K3))
            Y2 = mAdd(Y2,mScal(1/6,K4))
            Y2 = mAdd(Y1,mScal(h,Y2))
            vectMove(Y2,Y,n)
        return(h,t,Y)
    print("Hibás módszer megnevezés")
    return(h,t,y)


def diffEMilneHamming(FNF,Y00,a0,b0,N,eps=1e-6):
    "Milne-Hamming prediktor-korrektor módszer"
    M = len(Y00)
    h = (b0-a0)/N
    Y = DIM(4,N+1)
    Y0  = DIM(M)
    Y1  = DIM(M)
    Yn0 = DIM(M)
    Yn1 = DIM(M)
    Yn2 = DIM(M)
    Yn3 = DIM(M)
    Yn4 = DIM(M)
    Fn1 = DIM(M)
    Fn2 = DIM(M)
    Fn3 = DIM(M)
    F10 = DIM(M)
    F12 = DIM(M)
    t = DIM(N+1)
    # A szükséges kezdeti értékek kiszámítása 4-ed rendű Runge-Kutta módszerrel
    [h1,t1,Y] = diffERungeKutta(FNF,Y00,a0,a0+3*h,3,method="RK4")
    for i in range(4):
        t[i] = t1[i]
    n = 4
    # A 3. pontban a Milne prediktorával kapott érték, kezdetnek pontos értéket teszünk bele
    Yn0 = mdCol(Y,3)
    Yn1 = mdCol(Y,n-1)
    Yn2 = mdCol(Y,n-2)
    Yn3 = mdCol(Y,n-3)
    Yn4 = mdCol(Y,n-4)
    # Intervallumonkénti ciklus
    for n in range(4,N+1):
        t[n] = t[n-1]+h
        # A FI-értékei különböző t és y értékekre
        Fn1 = FNF(t[n-1],Yn1)
        Fn2 = FNF(t[n-2],Yn2)
        Fn3 = FNF(t[n-3],Yn3)
        Fn0 = FNF(t[n-1],Yn0)
        F12 = FNF(t[n-1],Yn2)
        # y[n) kezdeti értékének számítása Milne prediktorával
        Y0 = mAdd(mScal(2,Fn1),Fn2,"sub")
        Y0 = mAdd(Y0,mScal(2,Fn3))
        Y0 = mScal(4/3*h,Y0)
        Y0 = mAdd(Yn4,Y0)
        # Javító
        Y0 = mAdd(Y0,mScal(112/121*h,mAdd(Fn1,Fn0,"sub")))
        # A következő 0. közelítés
        Yn0 = mCopy(Y0)
        # Iteráció a korrektorral
        d = 100
        while( d>eps ):
            Y1 = mAdd(mScal(2,Fn1),F12,"sub")
            Y1 = mAdd(FNF(t[n],Y0),Y1)
            Y1 = mScal(3/8*h,Y1)
            Y1 = mAdd(Y1,mScal(1/8,mAdd(mScal(9,Yn1),Yn3,"sub")))
            d = vectAbs(mAdd(Y0,Y1,"sub"))
            Y0 = mCopy(Y1)
        # Korrektor iteráció vége. Az új pontot hozzá fűzzük az Y-hoz
        Y = mConcat(Y,Y1)
        Yn4 = mCopy(Yn3)
        Yn3 = mCopy(Yn2)
        Yn2 = mCopy(Yn1)
        Yn1 = mCopy(Y1)
    return(h1,t,Y)


# Bessel függvények (Gamma függvény)
####################################
def approxGamma(x,gx):
    "Közelítő kifejezés Gamma(x) számítására"
    # Csak a Gamma függvénnyel használható!!!!
    w = [-0.05149930,0.2548205,-0.5684729,0.8328212,
         -0.8764218,0.9858540,-0.577101]
    y = x-1
    gy = y*w[0]
    for i in range(1,7):
        gy = y*(gy+w[i])
    gy += 1
    gx = gx*gy
    return(gx)
    
def appGamma(x, err=1e-6):
    "Gamma függvény"
    if( x==1 ):
        return(1)
    gx = 1
    if( x>2 ):
        while( x>2 ):
            x -= 1
            gx *= x
        return(approxGamma(x,gx))
    if( x>1 ):
        return(approxGamma(x,gx))
    if( x>err and x<1):
        while( x>=1 ):
            gx /= x
            x += 1
        return(approxGamma(x,gx))
    print("x a hibahatáron belűl van")
    return


def logGamma(x):
    "log(Gamma) függvény közelítése Lánczos módszerrel"
    # A LanczosGamma függvényhez kell használni
    w = [1.000000000190015, 76.18009172947146, -86.50532032941677,
          24.01409824083091, -1.231739572450155, 0.0012086509738662,
          -0.000005395239385]
    if( x<0.5 ):
        lngx = log(pi/sin(pi*x))-logGamma(1-x)
        return(lngx)
    x = x-1
    b = x+5.5
    a = w[0]
    for i in range(1,7):
        a = a+w[i]/(x+i)
    lngx = (log(sqrt(2*pi))+log(a)-b)+log(b)*(x+0.5)
    return(lngx)
def LGamma(x):
    "Gamma függvény közelítése Lánczos módszerrel"
    # A logGamma függvényt kell használni
    return(exp(logGamma(x)))


def besJ(n,x,NMAX=50):
    "Elsőfajú Bessel függvények"
    # Gamma függvényen alapuló definíció alapján
    w = 0
    for i in range(NMAX):
        s1 = (-1)**i
        s2 = LGamma(i+1)
        s3 = LGamma(i+n+1)
        s4 = (x/2)**(2*i+n)
        w += (s1/(s2*s3))*s4
    return(w)


    
def BESJ(n,x):
    "Elsőfajú Bessel függvények"
    # H. Goldstein, R.M. Thaler módszerével
    d = 1e-6
    if( n<0 ):
        print("A függvény rendje negatív")
        return
    if( x<=0 ):
        print("Negatív x")
        return
    if( x<=15 ):
        NTEST = 20+10*x-x**2/3
    else:
        NTEST = 90+x/2
    if( n-NTEST>=0 ):
        print("n-hez x inkorrekt")
        return
    n1 = n+1
    bprev = 0
    if( x<5 ):
        ma = x+6
    else:
        ma = 1.4*x+60/x
    mb = n+round(x)/4+2
    mZero = round(max(ma,mb))
    mMax = round(NTEST)
    for m in range(mZero,mMax+1,3):
        fm1 = 1e-28
        fm = 0
        a = 0
        if( (m-(m/2)*2)==0 ):
            jt = -1
        else:
            jt = 1
        m2 = m-2
        for k in range(1,m2+1):
            mk = m-k
            bmk = 2*mk*fm1/x-fm
            fm = fm1
            fm1 = bmk
            if( (mk-n-1)==0 ):
                bj = bmk
            jt = -jt
            s = 1+jt
            a = a+bmk+s
        bmk = 2*fm1/x-fm
        if( n==0 ):
            bj = bmk
        a = a+bmk
        bj = bj/a
        if( abs(bj-bprev)-abs(d*bj)<=0 ):
            return(bj)
        bprev = bj
    return(bj)



def besYxGR4(x):
    "Segédfüggvény besY-hoz; x>4 eset"
    t1 = 4/x
    t2 = t1**2
    p0 = -0.0000037043*t2
    p0 = (p0+0.0000173565)*t2
    p0 = (p0-0.0000487613)*t2
    p0 = (p0+0.00017343)*t2
    p0 = (p0-0.001753062)*t2
    p0 = p0+0.3989423
    q0 = 0.0000032312*t2
    q0 = (q0-0.0000142078)*t2
    q0 = (q0+0.0000342468)*t2
    q0 = (q0-0.0000869791)*t2
    q0 = (q0+0.0004564324)*t2
    q0 = q0-0.01246694
    p1 = 0.0000042414*t2
    p1 = (p1-0.0000200920)*t2
    p1 = (p1+0.0000580759)*t2
    p1 = (p1-0.000223203)*t2
    p1 = (p1+0.002921826)*t2
    p1 = p1+0.3989423
    q1 = -0.0000036594*t2
    q1 = (q1+0.00001622)*t2
    q1 = (q1-0.0000398708)*t2
    q1 = (q1+0.0001064741)*t2
    q1 = (q1-0.0006390400)*t2
    q1 = q1+0.03740084
    a = 2/sqrt(x)
    b = a*t1
    c = x-0.7853982
    y0 = a*p0*sin(c)+b*q0*cos(c)
    y1 = -a*p1*cos(c)+b*q1*sin(c)
    return(y0,y1)
                  
def besY(n,x):
    "Másodfajú Bessel függvény"
    if( n<0 ):
        print("n negatív")
        return
    if( x>4 ):
        [y0,y1] = besYxGR4(x)
    if( x<=4 ):
        xx = x/2
        x2 = xx**2
        t = log(xx)+0.5772157
        s = 0
        term = t
        y0 = t
        for l in range(1,16):
            if( l!=1 ):
                s += 1/(l-1)
            fl = l
            ts = t-s
            term = (term*(-x2)/fl**2)*(1-1/(fl*ts))
            y0 += term
        term = xx*(t-0.5)
        s = 0
        y1 = term
        for l in range(2,17):
            s += 1/(l-1)
            fl = l
            fl1 = fl-1
            ts = t-s
            term = (term*(-x2)/(fl1*fl))*((ts-0.5/fl)/(ts+0.5/fl1))
            y1 += term
        pi2 = 0.6366198
        y0 =pi2*y0
        y1 = -pi2/x+pi2*y1
    if( n<0 ):
        return(y1)
    if( n==0 ):
        return(y0)
    if( n>0 and n<=1 ):
       return(y1)
    if( n>1 ):
        ya = y0
        yb = y1
        k = 1
        while( k-n<0 ):
            t = 2*k/x
            yc = t*yb-ya
            if( abs(yc)>1e70 ):
                print("Az eredmény 1e70 -nél nagyobb!!!!")
                return(yc)
            k += 1
            ya = yb
            yb = yc
        return(yc)

