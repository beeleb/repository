﻿from __future__ import division  # (p,q)区間をn-1等分するので小数が含まれる場合に対応させる
from numpy import linspace
from numpy import fabs
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
# ここから下に変数が入る


def f(x, a):
    return a*x-x**2  # 包絡線の式を入れる
FIGNUM = 1  # 0or1
if FIGNUM == 0:
    p, q, n = -2, 2, 13
if FIGNUM == 1:
    p, q, n = -3, 3, 31
# p:xの最小値, q:xの最大値, n:引く包絡線の数
a_min = -10  # 表示させるaの最小値
a_max = 10  # 表示させるaの最大値
y_min = -6  # 表示させるbの最小値(最大値はa軸とb軸の縮尺が1:1になるよう自動で決まる)
# アスペクト比を定めただけだと以上に縦長なグラフが出てくるのでylimを定めた
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
plt.figtext(0.85, 0.35, '$a$')  # 直接位置を指定している
plt.figtext(0.5, 0.95, '$b$')
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
plt.ylim(ymin=y_min)  # この位置より前に置くとx方向がが狭くなってしまった
plt.ylim(ymax=y_max)
a = linspace(a_min, a_max, (a_max-a_min) * 10)  # プロットする点の数はaが1増えるごとに10増えるようにした
for i in range(n):
    r = p+(q-p)*i/(n-1)  # n個の接線を引き2個は両端にあるので区間はn-1等分される
    b = f(r, a)
    ax.plot(a, b, 'k', linewidth=0.5, alpha=1)
# linewidth:線の太さ, alpha:濃さ(1以下), 黒色の線は'k'
plt.savefig('envelope'+str(FIGNUM)+'.png', bbox_inches='tight', pad_inches=0)
# plt.savefig('envelope'+str(FIGNUM)+'pdf', bbox_inches='tight', pad_inches=0)
# こちらはPDF保存用
