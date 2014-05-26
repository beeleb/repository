from __future__ import division #(p,q)区間をn-1等分するので小数が含まれる場合に対応させるため。
from pylab import * 
#pylabで数式をいろいろ定義してくれてるらしく、numpyいらなかったみたいです。
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt

#ここから下に変数が入っている。
def f(x,a):
	return a *x - x**2  #包絡線の式を入れる。
p = -3 #xの最小値
q = 3 #xの最大値
n = 12 #引く包絡線の数
a_min = -10 #表示させるaの最小値
a_max = 10 #表示させるaの最大値
y_min = -6 #表示させるbの最小値(最大値はa軸とb軸の縮尺が1:1になるよう自動で決まる)……アスペクト比を定めただけだと以上に縦長なグラフが出てくるので。
y_max = y_min + a_max - a_min #これは変数ではない

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

ax.axhline(linewidth=1.0, color="black")
ax.axvline(linewidth=1.0, color="black")

ax.set_xticks([])#ここに入れたx座標にticksが入る。
ax.set_yticks([])#ここに入れたy座標にticksが入る。
ax.set_xticklabels(['a'])#入れる文字
ax.set_yticklabels(['b'])#入れる文字……y軸側は横に90度回転してしまう。難しいか……？
#ここではちょっと下の直接入力をやっているので入れていない。最終的に直接入力を採用した場合はここは消す。
ax.set(aspect=1)

plt.figtext(0.85, 0.35, '$a$')#直接位置を指定している。この位置を変数使って表せればこれでいい……？
plt.figtext(0.5, 0.95, '$b$')

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)


ylim(ymin = y_min) 
ylim(ymax = y_max) 



a = linspace(a_min, a_max, (a_max - a_min) * 10) #特に根拠はないのですが,プロットする点の数はaが1増えるごとに10増えるようにしました。傾きが大きくなってくると厳しい……？
#aはiの値によらず一定の範囲なので、for文の外に出しました。
for i in range(n):
	r = p + (q - p) * i / (n - 1) #n個の接線を引き、2個は両端にあるので区間はn-1等分されるといいのかな、と考えました。
	b = f(r, a)
        ax.plot(a, b, 'k', linewidth=0.5, alpha=1) #linewidthは線の太さ、alphaは濃さ(1以下)をそれぞれ表す。黒色の線は'k'で指定する。指定しないとカラフルでそれはそれで見やすい。
show()
#plt.savefig('test1.png',bbox_inches='tight',dpi=150)
#上のは画像保存用。