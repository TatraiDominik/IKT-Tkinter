from tkinter import *
import math

foablak=Tk()
foablak.geometry("460x460")
s=''

def szamitas ():
    if not s:
        mezo4.delete(0, END)
        mezo4.insert(0, str("Szám adat kell"))

    r = float(mezo2.get())
    m = float(mezo3.get())
    borocska= float(mezo1.get())
    
    if r>0 and m>0:
            terfogat = round (math.pi * r * r * m /1000, )
            mezo4.delete (0, END)
            mezo4.insert (0, str(terfogat)+"dm3" )
            szazalek=round (borocska*(100/terfogat), )
            belefer= terfogat-borocska
            mezo6.delete (0, END)
            mezo6.insert (0, str(belefer)+"l" )
               
    elif r==0 or m==0:
        mezo4.delete(0, END)
        mezo4.insert(0, str("0 nem lehet adat"))
        mezo5.delete(0, END)
        mezo6.delete(0,END)
    else:
        mezo4.delete(0, END)
        mezo4.insert(0, str("pozitív szám kell"))

    if borocska>= terfogat:
        mezo5.delete(0,  END)
        mezo5.insert (0, str("Nem fér bele"))

    elif borocska<=0:   
        mezo5.delete(0, END)
        mezo5.insert(0, str("pozitív szám kell"))

    elif borocska==0:   
        mezo5.delete(0, END)
        mezo5.insert(0, str("0 nem lehet adat"))

    else:
        mezo5.delete (0, END)
        mezo5.insert(0, str(szazalek)+"%")

    if terfogat-borocska<=0 :
        mezo6.delete(0, END)
        mezo6.insert(0, str("Nem fér tőbb bor bele"))
    
cimke1=Label(foablak, text="Hány l bor?")
cimke1.grid(row=0, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=0, column=2)

sugar=Label(foablak, text="Henger alap sugara (cm)")
sugar.grid(row=1, column=1)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=2)

magassag=Label(foablak, text="Henger magassága(cm)")
magassag.grid(row=3, column=1)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=2)

kiszamitas=Button(foablak, text="kiszamitas", command=szamitas)
kiszamitas.grid(row=4, column=2)

eredmeny=Label(foablak, text="A hordó űrtartalma (l)")
eredmeny.grid(row=5, column=1)
mezo4=Entry(foablak)
mezo4.grid(row=5, column=2)

eredmeny2=Label(foablak, text="Ennyit foglal (%)")
eredmeny2.grid(row=6, column=1)
mezo5=Entry(foablak)
mezo5.grid(row=6, column=2)

eredmeny3=Label(foablak, text="Ennyi fér még bele")
eredmeny3.grid(row=7, column=1)
mezo6=Entry(foablak)
mezo6.grid(row=7, column=2)

foablak.mainloop()