from tkinter import *

foablak=Tk()

def ujablak():
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
    ablak2.mainloop()
    a=int(mezo1.get())
    b=int(mezo2.get())
    c=int(mezo3.get())
    felsz=2*(a*b+a*c+b*c)
    mezo4.delete(0,END)
    mezo4.insert(0, str(felszin))
    terf=a*b*c
    mezo5.delete(0, END)
    mezo5.insert(0, str(terfogat))

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

foablak.mainloop()