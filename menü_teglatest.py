from tkinter import *

foablak=Tk()

#felszin
def szamitas():

    ablak2=Toplevel(foablak)
    ablak2.geometry("300x300")

    mezo4=Entry(ablak2)
    mezo4.grid(row=0, column=1)
    mezo5=Entry(ablak2)
    mezo5.grid(row=1, column=1)

    aoldal=Label(foablak, text="a: ")
    aoldal.grid(row=1, column=0)
    mezo1=Entry(foablak)
    mezo1.grid(row=1, column=1)
    boldal=Label(foablak, text="b: ")
    boldal.grid(row=2, column=0)
    mezo2=Entry(foablak)
    mezo2.grid(row=2, column=1)
    coldal=Label(foablak, text="c: ")
    coldal.grid(row=3, column=0)
    mezo3=Entry(foablak)
    mezo3.grid(row=3, column=1)
    
    gomb1=Button(foablak, text="Számítás", command=ujablak)
    gomb1.grid(row=4, column=1)
    mezo4=Entry(ablak2)
    mezo4.grid(row=5, column=0)
    ablak2.mainloop()

    a=int(mezo1.get())
    b=int(mezo2.get())
    c=int(mezo3.get())
    felsz=2*(a*b+a*c+b*c)
    mezo4.delete(0,END)
    mezo4.insert(0, str(felszin))
    ablak3.mainloop()

#terfogat
def terfogat():

    ablak2=Toplevel(foablak)
    ablak2.geometry("300x300")
    felszin=Message(ablak2, text="Felszín")
    felszin.grid(row=0, column=0)
    terfogat=Message(ablak2, text="Terfogat")
    terfogat.grid(row=1, column=0)
    mezo4=Entry(ablak2)
    mezo4.grid(row=0, column=1)
    mezo5=Entry(ablak2)
    mezo5.grid(row=1, column=1)

    aoldal=Label(foablak, text="a: ")
    aoldal.grid(row=1, column=0)
    mezo1=Entry(foablak)
    mezo1.grid(row=1, column=1)
    boldal=Label(foablak, text="b: ")
    boldal.grid(row=2, column=0)
    mezo2=Entry(foablak)
    mezo2.grid(row=2, column=1)
    coldal=Label(foablak, text="c: ")
    coldal.grid(row=3, column=0)
    mezo3=Entry(foablak)
    mezo3.grid(row=3, column=1)

    gomb1=Button(foablak, text="Számítás", command=ujablak)
    gomb1.grid(row=4, column=1)
    ablak2.mainloop()

    def szamitas():
        a=int(mezo1.get())
        b=int(mezo2.get())
        c=int(mezo3.get())
        terf=a*b*c
        mezo5.delete(0, END)
        mezo5.insert(0, str(terfogat))
    ablak4.mainloop()

def nevjegy():
    ablak5=Toplevel(foablak)
    uz2=Message(ablak2, text="Készítette Tátrai Dominik\n2022.04.06", width=300)
    gomb2= Button(ablak2, text="Kilép", command=ablak2.destroy)
    uz2.grid()
    gomb2.grid()
    ablak5.mainloop()

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