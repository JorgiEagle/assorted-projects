from tkinter import *
master = Tk()
master.title('Counting coins')
w = Canvas(master, width = 100, height=100)
w.pack()
two_coins = IntVar()

compute_button = Button(master, text='Calculate', width=25, command=master.destroy)
compute_button.pack()
master.mainloop()
