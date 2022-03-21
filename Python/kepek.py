from tkinter import *
def klikk():
    print("Klikkeltem")


ablak1 = Tk()
gyoker = "H:\\IKT projekt\\Python\\"
ablak1.geometry("450x450")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file= gyoker+"xd.png")

ablak1.iconphoto(True, icon)
ablak1.config(bg='black')
elsokep = PhotoImage(file=gyoker+"spongebob-dancing.gif")
gombkep=PhotoImage(file=gyoker+"SB.gif")
cimke= Label(ablak1, 
                text="Üdvözlet!", 
                fg="cyan", 
                bg="#c3cee0", 
                font=("Arial", 45, "bold"), 
                bd=10, 
                relief=RAISED, 
                padx=25, 
                pady=30,
                image= elsokep,
                compound="center").pack()



gomb= Button(ablak1,
                text="Katitnts!",
                fg="blue",
                font=("Comic Sans", 35, "bold"),
                bg="yellow",
                relief=SUNKEN,
                bd=10,
                command=klikk,
                padx=12, 
                pady=12,
                image= gombkep,
                compound="bottom",
                activebackground="blue",
                activeforeground="yellow",
                state=ACTIVE).pack()

ablak1.mainloop()