from tkinter import *

foablak=Tk()

#felszin

     
    
def szamitas():
    def felszinsz():
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
#terfogat

def terfogat():
    def terfogatsz():
        a=int(mezo1.get())
        b=int(mezo2.get())
        c=int(mezo3.get())
        terf=a*b*c
        emezo.delete(0, END)
        emezo.insert(0, str(terf))

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

def nevjegy():
    ablak4=Toplevel(foablak)
    uz2=Message(ablak4, text="Készítette Tátrai Dominik\n2022.04.06", width=300)
    uz2.grid()
    gomb2= Button(ablak4, text="Kilép", command=ablak4.destroy)
    gomb2.grid()
    ablak4.mainloop()

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

foablak.mainloop()