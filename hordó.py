from tkinter import *
import math

foablak=Tk()

def szamitas ():
    r = int(mezo2.get())
    m = int(mezo3.get())
    borocska= int(mezo1.get())

    terfogat = round (math.pi * r * r * m /1000, 2)
    mezo4.delete (0, END)
    mezo4.insert (0, str(terfogat)+"dm3" )
    
    szazalek=round (borocska*(100/terfogat), 2)

    if borocska>= terfogat:
        mezo5.delete(0,  END)
        mezo5.insert (0, str("Nem fér bele"))

    elif borocska<=0:   
        mezo5.delete(0, END)
        mezo5.insert(0, str("0 nem lehet adat"))

    else:
        mezo5.delete (0, END)
        mezo5.insert(0, str(szazalek)+"%")
    
    
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


foablak.mainloop()