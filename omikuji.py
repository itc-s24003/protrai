# s24003
# GUIで動くおみくじ
import tkinter as tk
root = tk.Tk()
root.geometry("500x300")
import random
omikuji = ["大吉","中吉","小吉","凶","大凶","反吉","末吉","大大吉"]
lbl=tk.Label(text=random.choice(omikuji))
lbl.pack()
root.mainloop()
