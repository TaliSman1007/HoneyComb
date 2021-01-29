# Info box

import time
import datetime

try:
    import Tkinter as tk
except:
    import tkinter as tk

# Main Window
root = tk.Tk(className = "Info")
root.geometry("260x284")
root.title("Info")
root.option_add("*Font", "TkDefaultFont 9")
root.config(padx=2, pady=2)

# title
frame1 = tk.Frame()
frame1.pack(fill='x')
label1 = tk.Label(frame1, anchor='w', text="Title: ", width=6)
label1.pack(side='left', padx=4, pady=4)           
entry1 = tk.Entry(frame1)
entry1.insert('end', "Texpert ")
entry1.config(state='readonly')
entry1.pack(fill='x', padx=4, expand=True)
        
# author
frame2 = tk.Frame()
frame2.pack(fill='x')
label2 = tk.Label(frame2, anchor='w', text="Author: ", width=6)
label2.pack(side='left', padx=4, pady=4)        
entry2 = tk.Entry(frame2)
entry2.insert('end', "TaliSman")
entry2.config(state='readonly')
entry2.pack(fill='x', padx=4, expand=True)
   
# credits     
frame3 = tk.Frame()
frame3.pack(fill='both', expand=True)
label3 = tk.Label(frame3, anchor='w', text="Credits: ", width=6)
label3.pack(side='left', anchor='n', padx=4, pady=4)        
txt = tk.Label(frame3, height=10, text="Created by TaliSman")
txt.config(state='disabled')
txt.pack(fill='x', pady=4, padx=4, expand=True)

# buttons
closeButton = tk.Button(text="Close", command=root.destroy)
closeButton.pack(side='right', padx=4, pady=4)

root.mainloop()  
