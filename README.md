# missing bars in matplotlib.pyplot.bar()

* 증상: matplotlib.pyplot.bar()로 막대 그래프를 그릴 때 막대가 사라지거나 막대 사이의 틈이 사라지는 현상이 있음

* 원인: matplotlib.pyplot.bar()는 막대를 무조건 1픽셀 단위로만 그림

* 해결책: bar()의 파라미터 중 width를 조절, 필요에 따라 figsize를 조절하거나 edgecolor를 넣거나 Figure 창의 크기를 조절
