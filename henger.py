from tkinter import *

foablak=Tk()
def kiszamit():
    r=int(mezo1.get())
    m=int(mezo2.get)
    eredmeny=3,14*r*r*m
    mezo3.delete(0, END)
    mez3.insert(0, +str(eredmeny))

cimke1=Label (foablak, text="Sugár (cm):" )
cimke1.grid(row=1, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=2)

cimke2=Label (foablak, text="Magasság (cm):" )
cimke2.grid(row=2, column=1)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=2)

gomb1=Button(foablak, text="Kiszámít", command=kiszamit)
gomb1.grid(row=3, column=1, sticky='e')

cimke3=Label (foablak, text="Térfogat)" )
cimke3.grid(row=4, column=1)
mezo3=Entry(foablak)
mezo3.grid(row=4, column=2)

cimke4=Label (foablak, text="Vashenger" )
cimke4.grid(row=5, column=1)
mezo4=Entry(foablak)
mezo4.grid(row=5, column=2)

cimke5=Label (foablak, text="Fahenger" )
cimke5.grid(row=6, column=1)
mezo5=Entry(foablak)
mezo5.grid(row=6, column=2)

foablak.mainloop()