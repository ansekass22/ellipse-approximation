from tkinter import *
import tkinter
from tkinter import font
from tkinter import messagebox
import ellipsiApprox as eApp
import ellipseApproxPlot as eap

#############################################################
# (C) Antti Kasslin
# 2022
#############################################################
# Ohjelma, jolla voidaan tehdä ellipsiä mahdollisimman
# jäljitteleviä monikulmioita, eli ellipsiapproksimaatioita.
#############################################################
def valintaToiminto():
    if var1.get() == 1:
        
        valinta2.configure(state='normal')
        valinta3.configure(state='normal')
        valinta4.configure(state='normal')
    else:
        valinta2.configure(state='disabled')
        valinta3.configure(state='disabled')
        valinta4.configure(state='disabled')

def suoritus():#---TÄHÄN ASTI MUOKATTU---
    PI = 3.14159265 #piin likiarvo
    sade1 = int(sadeValitsin1.get())#käyttäjä antaa ellipsin 1. akselin
    sade2 = int(sadeValitsin2.get())#käyttäjä antaa ellipsin 2. akselin
    labelWarn.config(text="")
    try:
        tarkkuus = float(tarkkuusValitsin.get()) #käyttäjä antaa tarkkuusparametrin, joka määrittää mitä pisteitä valitaan approksimaatioon
    except ValueError:
        messagebox.showwarning("HUOM!", "Tarkkuuden pitäisi olla numeromuodossa!")
    if tarkkuus < 0.1:#HUOM! Nämä rajat pitää vielä määrittää ellipsiapproksimaatiolle tarkemmin
        labelWarn.config(text="Huom! Liian pieni tarkkuus tekee \napproksimaatiosta neliömäisen!",fg="red")
    if tarkkuus > 0.5:
        labelWarn.config(text="Huom! Liian suuri tarkkuus tekee \napproksimaation reunasta porrasmaisen!",fg="red")
 
    neljannesX,neljannesY,polkuX,polkuY = eApp.ellipsiApprox(sade1,sade2,tarkkuus)
    neljPlusOrigoX,neljPlusOrigoY = neljannesX[:],neljannesY[:]
    neljPlusOrigoX.append(0) #origo lisätään tähän pistejoukkoon
    neljPlusOrigoY.append(0) #neljännespinta-alan laskemiseksi
    neljPintaAla = eApp.shoeLace(neljPlusOrigoX,neljPlusOrigoY)
    neljPiiri = eApp.piirinPituus(neljannesX,neljannesY)

    neljannesX, neljannesY = eApp.taydennaApprox(neljannesX,neljannesY)

    pa1.delete(0,END)       #tyhjennetään 
    piiri1.delete(0,END)    #edelliset lukemat
    pa2.delete(0,END)       #ennen kuin
    #piiri2.delete(0,END)    #uudet lisätään
    pa1.insert(0,str(4*neljPintaAla))
    piiri1.insert(0,str(4*neljPiiri))
    pa2.insert(0,str(PI*sade1*sade2))
    #piiri2.insert(0,str(PI*2*sade))

    if var1.get() == 1:
        eap.makePlot(sade1,sade2,tarkkuus,neljannesX,neljannesY,polkuX,polkuY,var2,var3,var4)

# käyttöliittymän alustusta
juuri = Tk()
juuri.title("Ympyräapproksimaatio")
juuri.geometry('500x400')

# käyttöliittymän toimintojen sijoittelua
label1 = Label(juuri, text="Valitse vaaka-akselin pituus")
sadeValitsin1 = Spinbox(juuri,from_=1,to=50,bd=5)
label1.grid(row=0,column=0,padx=5,pady=5)
sadeValitsin1.grid(row=0,column=1,padx=5,pady=5)

label1 = Label(juuri, text="Valitse pystyakselin pituus")
sadeValitsin2 = Spinbox(juuri,from_=1,to=50,bd=5)
label1.grid(row=1,column=0,padx=5,pady=5)
sadeValitsin2.grid(row=1,column=1,padx=5,pady=5)

label2 = Label(juuri, text="Valitse tarkkuus")
tarkkuusValitsin = Entry(juuri, justify='right', bd='5')
label2.grid(row=2,column=0,padx=5,pady=5)
tarkkuusValitsin.grid(row=2,column=1,padx=5,pady=5)
labelWarn = Label(juuri, text="") 
labelWarn.grid(row=2,column=2) #varoitusteksti, jos epäsopiva tarkkuus

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
valinta1 = Checkbutton(juuri,text='Näytä kuvaaja', justify='left',variable=var1, onvalue=1, offvalue=0, state='normal', command=valintaToiminto)
valinta2 = Checkbutton(juuri,text='Näytä approksimaatio', justify='left',variable=var2, onvalue=1, offvalue=0, state='disabled')
valinta3 = Checkbutton(juuri,text='Näytä ellipsi           ', justify='left',variable=var3, onvalue=1, offvalue=0, state='disabled')
valinta4 = Checkbutton(juuri,text='Näytä algoritmipolku  ', justify='left',variable=var4, onvalue=1, offvalue=0, state='disabled')
valinta1.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
valinta2.grid(row=4,column=1)
valinta3.grid(row=5,column=1)
valinta4.grid(row=6,column=1)

kaynnistys = Button(juuri,text="Suorita approksimaatio",command=suoritus, width=20, font=15)
kaynnistys.grid(row=7, column=0,columnspan=3,padx=5,pady=5)#tarkista, tarvitaanko columnspan=4

label3 = Label(juuri, text="APPROKSIMAATIO")
label4 = Label(juuri, text="OIKEA ELLIPSI")
label3.grid(row=8,column=1,padx=5,pady=5)
label4.grid(row=8,column=2,padx=5,pady=5)
label5 = Label(juuri, text="Pinta-ala:")
label6 = Label(juuri, text="Piiri:")
label5.grid(row=9,column=0,padx=5,pady=5)
label6.grid(row=10,column=0,padx=5,pady=5)
pa1 = Entry(juuri, justify='right', bd='5')
pa2 = Entry(juuri, justify='right', bd='5')
piiri1 = Entry(juuri, justify='right', bd='5')
#piiri2 = Entry(juuri, justify='right', bd='5')TARPEETON
pa1.grid(row=9,column=1,padx=5,pady=5)
pa2.grid(row=9,column=2,padx=5,pady=5)
piiri1.grid(row=10,column=1,padx=5,pady=5)
#piiri2.grid(row=9,column=2,padx=5,pady=5)TARPEETON

juuri.mainloop()