from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.ticker import MultipleLocator

#############################################################
# (C) Antti Kasslin
# 2022
#############################################################
# Tässä moduulissa hoidetaan ellipsiApproksimaatio.py:n
# vaatiman kuvaajien teko.
#############################################################
def makePlot(R1,R2,dr,pointsX,pointsY,pathX,pathY,var2,var3,var4):
    if var2.get() == 1: #approksimaatio piirretään kuvaajaan,vain jos käyttäjä niin valitsee
        plt.plot(pointsX, pointsY, 'ko-')
    plt.axis([-(R1+2),R1+2,-(R2+2),R2+2]) #kuvaajan koko ei tarvitse olla paljon ympyrän kokoa suurempi
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.xaxis.set_minor_locator(MultipleLocator(1.0)) # approksimaation pisteitä on helpompi seurata
    ax.yaxis.set_minor_locator(MultipleLocator(1.0)) # jos kuvaajassa on 1x1 ruudukko
    if var3.get() == 1: #varsinainen ympyrä piirretään kuvaajaan,vain jos käyttäjä niin valitsee
        ellipse = Ellipse((0,0), R1*2, R2*2, fill=True, color='yellow')
        plt.gca().add_patch(ellipse)
    if var4.get() == 1: #polkualgoritmin reitti  piirretään kuvaajaan,vain jos käyttäjä niin valitsee
        plt.plot(pathX,pathY, 'r:')
    plt.title("Vaaka-akseli:"+str(R1)+" Pystyakseli:"+str(R2)+", tarkkuus:"+str(dr))
    plt.grid(True)
    plt.grid(which='minor',axis='x')
    plt.grid(which='minor',axis='y')
    plt.show()
    