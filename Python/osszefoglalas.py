from tkinter import *

foablak = Tk()

elsomezo = Label (foablak, text='Első mező:')
elsomezo.grid (column=1, row=1)

masodiksor = Label (foablak, text='Második mező:')
masodiksor.grid (column=1, row=2)

harmadiksor = Label (foablak, text='Harmadik mező:')
harmadiksor.grid (column=1, row=3)


elso = Entry (foablak)
elso.grid (column=2, row=1)

masodik = Entry (foablak)
masodik.grid (column=2, row=2)

harmadik = Entry (foablak)
harmadik.grid (column=2, row=3)

can1 = Canvas(foablak,
            width = 160,
            height = 160,
            bg = 'white')
can1.grid (column=3, row=1, rowspan=3)
photo = PhotoImage(file='xd.png')
photo.subsample(2,2)
item = can1.create_image(80,80,image= photo)

icon = PhotoImage(file='spongenon.png')
foablak.iconphoto(True, icon)

foablak.mainloop()