import Tkinter as Tk
import os,sys, subprocess
from threading import Timer

def exit_fun ():
	os._exit(0)
text_col = "white"
bg_col = "#090e11"
root = Tk.Tk()
root.title("Enter pattern")

root.attributes("-alpha",0)
root.configure(background=bg_col)
w,h= 500,300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
p = os.popen("motivate")
text_me =str(p.read())
text_me = text_me.lstrip("\033[1;36m" + "\"")
quote = text_me[:text_me.find( "\"" + "\033[1;m" + "\n\t\t"+ "\033[1;35m" + "--")]
text_me = text_me.lstrip(quote +  "\"" + "\033[1;m" + "\n\t\t"+ "\033[1;35m" + "--")
author = text_me[:text_me.find("\033[1;m")]

Timer(6.0, exit_fun).start()
#quote = quote.replace(".",".\n")


Tk.Label(root, pady=10, text="Quote for the day!",fg="#64d671",bg=bg_col,wraplength = w-30,font = "Helvetica 15 bold italic").pack()
Quote_l = Tk.Label(root,text="\"" + quote + "\"",pady = h/6,fg=text_col,bg=bg_col,wraplength = w-30,font = "Arial 12 bold italic")
Author_l = Tk.Label(root,text=" - " +author,fg="#ff8484",bg=bg_col, font= "times_new_roman 11 italic")
Quote_l.pack()
Author_l.pack()
b1 = Tk.Button(root,text="   ", justify =Tk.LEFT,command = "exit")
b1.config(activebackground = "#cc8251")
b1.pack(pady = 10)
root.mainloop()
