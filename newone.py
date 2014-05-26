from __future__ import division #(p,q)区間をn-1等分するので小数が含まれる場合に対応させるため。
from pylab import * 
#pylabで数式をいろいろ定義してくれてるらしく、numpyいらなかったみたいです。
import matplotlib.pyplot as plt
def subplots():
#このへんまだよくわからないです。目盛りは消えたけど軸に矢印がついてないし軸の名前の位置も違う。さらにb軸は向きも違う。
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()
    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    ax.set(aspect=1) #アスペクト比を固定しました。
    ax.set_xticks([]) 
    ax.set_yticks([])
    xlabel("a", fontname='serif') # x軸のタイトル
    ylabel(r"b", fontname='serif') # y軸のタイトル
    return fig, ax
    
fig, ax = subplots()

#ここから下に変数が入っている。
def f(x,a):
	return a *x - x**2  #包絡線の式を入れる。
p = -3 #xの最小値
q = 3 #xの最大値
n = 12 #引く包絡線の数
a_min = -10 #表示させるaの最小値
a_max = 10 #表示させるaの最大値
y_min = -6 #表示させるbの最小値(最大値はa軸とb軸の縮尺が1:1になるよう自動で決まる)……アスペクト比を定めただけだと以上に縦長なグラフが出てくるので。
ylim(ymin = y_min) 
ylim(ymax= y_min + a_max - a_min) 
#変数ここまで。下3つは自動で定められると嬉しいけど……？



a = linspace(a_min, a_max, (a_max - a_min) * 10) #特に根拠はないのですが,プロットする点の数はaが1増えるごとに10増えるようにしました。傾きが大きくなってくると厳しい……？
#aはiの値によらず一定の範囲なので、for文の外に出しました。
for i in range(n):
	r = p + (q - p) * i / (n - 1) #n個の接線を引き、2個は両端にあるので区間はn-1等分されるといいのかな、と考えました。
	b = f(r, a)
        ax.plot(a, b, 'k', linewidth=0.5, alpha=1) #linewidthは線の太さ、alphaは濃さ(1以下)をそれぞれ表す。黒色の線は'k'で指定する。指定しないとカラフルでそれはそれで見やすい。
show()	
#定めた範囲内で包絡線すべてがおさまるように表示するbの範囲を(自動的に)決めているようなので、肝心の放物線(など)が小さく表示されすぎてしまう……。要改善。
#bの値が一定以下になったところで切りたいけど、グラフによって「切りたい値」は変わってくる……？
#プロットされたグラフを表示する際、a軸とb軸の比率は1:1になっているのか……？(なっていないような気がする)→aの最小、最大を用いてbの範囲も定められないか……？