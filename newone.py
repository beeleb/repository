from __future__ import division #(p,q)区間をn-1等分するので小数が含まれる場合に対応させるため。
from pylab import * 
#pylabで数式をいろいろ定義してくれてるらしく、numpyいらなかったみたいです。
import matplotlib.pyplot as plt

def subplots(): #このへんまだよくわからないです。細かい目盛りを消して軸に矢印を入れたい。
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    ax.grid()
    return fig, ax
fig, ax = subplots()
def f(x,a):
	return -x**2 + a*x #包絡線の式を入れる。
p = -10 #左端のa
q = 10 #右端のa
n = 50 #引く包絡線の数
for i in range(n):
	r = p + (q - p) * i / (n - 1) #n個の接線を引き、2個は両端にあるので区間はn-1等分されるといいのかな、と考えました。
	a = linspace(p, q, (q-p) * 10) #特に根拠はないのですが,プロットする点の数はaが1増えるごとに10増えるようにしました。傾きが大きくなってくると厳しい……？
	b = f(r, a)
        ax.plot(a, b, 'b-', linewidth=1, alpha=0.3) #linewidthは線の太さ、alphaは濃さ(1以下)をそれぞれ表す。
show()	