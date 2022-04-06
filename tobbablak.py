from tkinter import *

foablak=Tk()

def ujablak():
    ablak2=Toplevel(foablak)
    uz2=Message(ablak2, text="Készítette Gipsz Jakab\nPiripócs\n2009.06.04", width=300)
    gomb2= Button(ablak2, text="Kilép", command=ablak2.destroy)
    uz2.pack()
    gomb2.pack()
    ablak2.mainloop()

szoveg1=Label(foablak, text="Kattints a gombra!")
szoveg1.pack()
gomb1=Button(foablak, text="Névjegy", command=ujablak)
gomb1.pack()



foablak.mainloop()