import tkinter as tk
import os
import random

root = tk.Tk()
root.title("Motivation")
root.configure(background='white')
command=os.getcwd()+'/motivate/motivate.py'
quote=os.popen(command).read()
color=random.choice(['green','blue','purple','red','orange','brown','magenta','violet','maroon','olive','lime','teal','navy','DarkSlateGray','m','indigo','crimson'])
label=tk.Label(root, text = quote ,fg=color, bg='white', font='Helvetica 10',wraplength=900).pack()
quit_btn=tk.Button(root,text="Quit",command=root.destroy)
quit_btn.pack(side="bottom")
root.mainloop()

