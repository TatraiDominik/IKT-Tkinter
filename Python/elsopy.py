from tkinter import *
def osszeg():
    a= int(mezo1.get())
    b= int(mezo2.get())
    c= a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))
 
def kivon():
    a= int(mezo1.get())
    b= int(mezo2.get())
    c= a - b
    mezo3.delete(0, END)
    mezo3.insert(0, "Különbség: "+str(c))


def szorzas():
    a= int(mezo1.get())
    b= int(mezo2.get())
    c= a * b
    mezo3.delete(0, END)
    mezo3.insert(0, "Szorzat: "+str(c))

def osztas():
    a= int(mezo1.get())
    b= int(mezo2.get())
    if b==0:
        mezo3.delete(0, END)
        mezo3.insert(0, "Error-nullával nem lehet osztani")
    else:
        c= a / b
        mezo3.delete(0, END)
        mezo3.insert(0, "Hányados: "+str(c))

def négyzet():
    a= int(mezo1.get())
    c= a * a
    mezo3.delete(0, END)
    mezo3.insert(0, "Négyzete: "+str(c))

def gyokvonas():
    import math
    a= int(mezo1.get())
    if a < 0:
        mezo3.insert(0, "Error-negatív számból nem lehet gyököt vonni")
    else:
        c= math.sqrt(a)
        mezo3.delete(0, END)
        mezo3.insert(0, "Gyöke: "+str(c))

foablak=Tk()
foablak.config(bg="gray")
cimke=Label(foablak,text="Üdvözlet!", fg="red")
cimke.grid()



cimke=Label(foablak, text="Első szám")
cimke.grid(row=0, column=0)
mezo1=Entry(foablak)
mezo1.grid(row=0, column=2)

cimke=Label(foablak, text="Második szám")
cimke.grid(row=1, column=0)
mezo2=Entry(foablak)
mezo2.grid(row=1, column=2)


gomb4=Button(foablak, text="Összead", command=osszeg)
gomb4.grid(row=2, column=1)

gomb5=Button(foablak, text="Kivon", command=kivon)
gomb5.grid(row=3, column=1)

gomb6=Button(foablak, text="Szorzás", command=szorzas, fg="green")
gomb6.grid(row=3, column=1)

gomb7=Button(foablak, text="Osztás", command=osztas, fg="blue")
gomb7.grid(row=4, column=1)

gomb8=Button(foablak, text="Négyzetre emelés", command=négyzet, )
gomb8.grid(row=5, column=1)

gomb9=Button(foablak, text="Gyökvonás", command=gyokvonas )
gomb9.grid(row=6, column=1)

mezo3=Entry(foablak)
mezo3.grid(row=7, column=1)

gomb3=Button(foablak, text="Kilépés", command=foablak.destroy)
gomb3.grid(row=8, column=2)



can1= Canvas(foablak, width=460, height=229, bg="white")
photo = PhotoImage(file="SB.gif")
item = can1.create_image(300,114, image= photo)
can1.grid(row=9, column=1)

foablak.mainloop()