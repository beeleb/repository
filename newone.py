import matplotlib.pyplot as plt
import numpy as np

def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    ax.grid()
    return fig, ax
#まず関数f(x)に関して
#このあたりからfor文使って接線を一本一本描いてくといいのかな？本数をnで指定させてfor i……とか。
#最初に指定した区間[a,b]をn分割させてx=aにおける接線、x=a+((b-a)/n)における接線、……x=bにおける接線、とやりたい。
#接線をどうやって求めるか？微分しなくてはいけないけど……？→Sympyからdiffを用いて微分係数を求められるので意外とラクに行けるか……？


fig, ax = subplots()  # Call the local version, not plt.subplots()
x = np.linspace(-2, 10, 200) #左から順番にグラフの左端のx座標、右端のx座標、打つ点の数……課題では後から入れられるようにしたい。
y = np.sin(x)　#プロットの対象とする関数……課題ではこれも後から入れられるようにしたい
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)　#linewidthは線の太さ、labelはlegend内の文字、alphaは濃さ(1以下)をそれぞれ表す。
ax.legend(loc='lower right')
plt.show()