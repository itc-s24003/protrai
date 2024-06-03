#turtle1.py

from turtle import *#タートルグラフィックス
shape("turtle")#カメの登場
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()#おしまい
