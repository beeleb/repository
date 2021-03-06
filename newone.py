﻿from __future__ import division  # (p,q)区間をn-1等分するので小数が含まれる場合に対応させる
from numpy import linspace
from numpy import fabs
from numpy import array
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
# ここから下に変数が入る


def f(x, a):
    return a*x-x**2  # 包絡線の式を入れる
p = -3  # xの最小値
q = 3  # xの最大値
n = 12  # 引く包絡線の数
a_min = -10  # 表示させるaの最小値
a_max = 10  # 表示させるaの最大値
y_min = -6  # 表示させるbの最小値(最大値はa軸とb軸の縮尺が1:1になるよう自動で決まる)
# アスペクト比を定めただけだと異常に縦長なグラフが出てくるのでylimを定めた
y_max = y_min+a_max-a_min  # これは変数ではない
plt.figtext(0.85, 0.35, '$a$')  # 直接位置を指定しているので、グラフの位置を変えるときにこれも変える
plt.figtext(0.5, 0.95, '$b$')
# ここより上に変数が入る
fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
ax.axhline(linewidth=1.0, color="black")
ax.axvline(linewidth=1.0, color="black")
ax.set_xticks([])  # 空のlistを指定することでticksが入らない
ax.set_yticks([])
ax.set(aspect=1)
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
plt.ylim(ymin=y_min)  # この位置より前に置くとx方向が狭くなってしまった
plt.ylim(ymax=y_max)
a = linspace(a_min, a_max, (a_max-a_min) * 10)  # 点の数はaの動く範囲の長さ×10,これで曲線にも対応する
# linspaceの点の数に小数が来ることがあり得るのですが、その場合は勝手に小数点以下を切り捨てた数の点をとってくれるようです
for i in range(n):
    r = p+(q-p)*i/(n-1)  # n個の接線を引き2個は両端にあるので区間はn-1等分される
    b = f(r, a)
    ax.plot(a, b, 'k', linewidth=0.5, alpha=1)
# linewidth:線の太さ, alpha:濃さ(1以下), 黒色の線は'k'
plt.show()
# plt.savefig('envelopeX.png', bbox_inches='tight', pad_inches=0)
# plt.savefig('test2.pdf,bbox_inches='tight',pad_inches=0)
# それぞれ画像保存用,PDF保存用