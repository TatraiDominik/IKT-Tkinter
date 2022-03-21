from tkinter import *

foablak= Tk()
foablak.geometry("450x450")



cimke1=Label(foablak, text="Első mező",
                    fg="black")
cimke1.grid(row=1, column=1)
mezo1=Entry(foablak)
mezo1.grid(row=1, column=2)

cimke2=Label(foablak, text="Második mező",
                    fg="black")
cimke2.grid()

mezo2=Entry(foablak)
mezo2.grid(row=2, column=1)
cimke3=Label(foablak, text="Harmadik mező",
                    fg="black")                   
cimke3.grid()

mezo3=Entry(foablak)
mezo3.grid()
foablak.mainloop()