#GUIで動くアプリを作ってみるよ

import tkinter as tk#この行を書く必要があるよ
root = tk.Tk()#初めのおまじない

root.geometry("500x300")#運動のサイズを決める
root.title("ハローアプリ")#ウィンドウのタイトルを決める
lbl=tk.Label(text="こんにちは世界")
lbl.pack()
lbl=tk.Label(text="初めてのGUIアプリ")
lbl.pack()#lblを配置させる必要があるよ

root.mainloop()#終わりのおまじない
