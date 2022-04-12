from tkinter import *
import math
foablak=Tk()

#felszin T
s=''        
def szamitas():
    def felszinsz():
        if not s:
            emezo.delete(0, END)
            emezo.insert(0, str("Szám adat kell"))

        a=int(mezo1.get())
        b=int(mezo2.get())
        c=int(mezo3.get())

        if a>0 or b>0 or c>0:
            felsz=2*(a*b+a*c+b*c)
            emezo.delete(0,END)
            emezo.insert(0, str(felsz))

        else:
            emezo.delete(0,END)
            emezo.insert(0, str("pozitív szám kell"))

    ablak2=Toplevel(foablak)
    ablak2.geometry("300x300")

    aoldal=Label(ablak2, text="a: ")
    aoldal.grid(row=1, column=0)
    mezo1=Entry(ablak2)
    mezo1.grid(row=1, column=1)
    boldal=Label(ablak2, text="b: ")
    boldal.grid(row=2, column=0)
    mezo2=Entry(ablak2)
    mezo2.grid(row=2, column=1)
    coldal=Label(ablak2, text="c: ")
    coldal.grid(row=3, column=0)
    mezo3=Entry(ablak2)
    mezo3.grid(row=3, column=1)

    gomb1=Button(ablak2, text="Számítás", command=felszinsz)
    gomb1.grid(row=4, column=1)
    erdemeny=Label(ablak2,text="Eredmény:")
    erdemeny.grid(row=5, column=0)
    emezo=Entry(ablak2)
    emezo.grid(row=5, column=1)
    
    ablak2.mainloop()

#terfogat T
def terfogat():
    def terfogatsz():

        if not s:
            emezo.delete(0, END)
            emezo.insert(0, str("Szám adat kell"))

        a=int(mezo1.get())
        b=int(mezo2.get())
        c=int(mezo3.get())

        if a>0 or b>0 or c>0:
            terf=a*b*c
            emezo.delete(0, END)
            emezo.insert(0, str(terf))
        else:
            emezo.delete(0, END)
            emezo.insert(0, str("Pozitív szám kell"))

    ablak3=Toplevel(foablak)
    ablak3.geometry("300x300")
    
    aoldal=Label(ablak3, text="a: ")
    aoldal.grid(row=1, column=0)
    mezo1=Entry(ablak3)
    mezo1.grid(row=1, column=1)
    boldal=Label(ablak3, text="b: ")
    boldal.grid(row=2, column=0)
    mezo2=Entry(ablak3)
    mezo2.grid(row=2, column=1)
    coldal=Label(ablak3, text="c: ")
    coldal.grid(row=3, column=0)
    mezo3=Entry(ablak3)
    mezo3.grid(row=3, column=1)
    
    gomb1=Button(ablak3, text="Számítás", command=terfogatsz)
    gomb1.grid(row=4, column=1)
    eredmeny=Label(ablak3, text="Eredmény")
    eredmeny.grid(row=5, column=0)
    emezo=Entry(ablak3)
    emezo.grid(row=5, column=1)
    ablak3.mainloop()
#terfogat vége

#Felszín H
def hengerterf():
    def Hterfogatszam():
        r = int(mezo1.get())
        m = int(mezo2.get())
        terfogat = round (math.pi * r * r * m, 2)
        emezo.delete (0, END)
        emezo.insert (0, str(terfogat))

    ablak5=Toplevel(foablak)

    suagr=Label(ablak5, text="Sugár: ")
    suagr.grid(row=1, column=0)
    mezo1=Entry(ablak5)
    mezo1.grid(row=1, column=1)
    magassag=Label(ablak5, text="Magasság: ")
    magassag.grid(row=2, column=0)
    mezo2=Entry(ablak5)
    mezo2.grid(row=2, column=1)
    
    gomb1=Button(ablak5, text="Számítás", command=Hterfogatszam)
    gomb1.grid(row=4, column=1)
    eredmeny=Label(ablak5, text="Eredmény")
    eredmeny.grid(row=5, column=0)
    emezo=Entry(ablak5)
    emezo.grid(row=5, column=1)

    ablak5.mainloop()

def Hfelszin():
    def Hfelszinszam():
        r = int(mezo1.get())
        m = int(mezo2.get())
        if not s:
            emezo.delete(0, END)
            emezo.insert(0, str("Szám adat kell"))
        if r>0 or m>0:
            felszin = round (2*r*r*math.pi+2*r*math.pi*m )
            emezo.delete (0, END)
            emezo.insert (0, str(felszin))
        else:
            emezo.delete(0, END)
            emezo.insert(0, str("Pozitív szám kell"))
    ablak6=Toplevel(foablak)
    suagr=Label(ablak6, text="Sugár: ")
    suagr.grid(row=1, column=0)
    mezo1=Entry(ablak6)
    mezo1.grid(row=1, column=1)
    magassag=Label(ablak6, text="Magasság: ")
    magassag.grid(row=2, column=0)
    mezo2=Entry(ablak6)
    mezo2.grid(row=2, column=1)
    
    gomb1=Button(ablak6, text="Számítás", command=Hfelszinszam)
    gomb1.grid(row=4, column=1)
    eredmeny=Label(ablak6, text="Eredmény")
    eredmeny.grid(row=5, column=0)
    emezo=Entry(ablak6)
    emezo.grid(row=5, column=1)
    ablak6.mainloop()
#névjegy
def nevjegy():
    ablak4=Toplevel(foablak)
    uz2=Message(ablak4, text="Készítette Tátrai Dominik\n2022.04.06", width=300)
    uz2.grid()
    gomb2= Button(ablak4, text="Kilép", command=ablak4.destroy)
    gomb2.grid()
    ablak4.mainloop()
#névjegy vége

menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

#Fájl
menu1=Menubutton(menusor, text="Fájl", underline=0)
menu1.pack(side=LEFT)
fajl= Menu(menu1)
fajl.add_command(label="Névjegy", command=nevjegy, underline=0)
fajl.add_command(label="Kilépés", command=foablak.destroy, underline=0)
menu1.config(menu=fajl)

#Téglatest
menu2= Menubutton(menusor, text="Téglatest", underline=0)
menu2.pack(side=LEFT)
teglatest= Menu(menu2)
teglatest.add_command(label="Felszín", command=szamitas, underline=0)
teglatest.add_command(label="Térfogat", command=terfogat, underline=0)
menu2.config(menu=teglatest)

#Henger
menu3= Menubutton(menusor, text="Henger", underline=0)
menu3.pack(side=LEFT)
henger=Menu(menu3)
henger.add_command(label="Felszín", command=Hfelszin, underline=0)
henger.add_command(label="Térfogat", command=hengerterf, underline=0)
menu3.config(menu=henger)
foablak.mainloop()