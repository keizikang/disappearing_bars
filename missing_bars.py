import matplotlib.pyplot as plt


# 10개짜리 bar graph
plt.bar(range(1, 11), range(1, 11))
plt.show()


# 100개짜리 bar graph
plt.bar(range(1, 101), range(1, 101))
plt.show()


# 100개짜리 bar graph - Figure 폭 바꿈
plt.figure(figsize=(5, 4))
plt.bar(range(1, 101), range(1, 101))
plt.show()


# bar width 조절
plt.bar(range(1, 101), range(1, 101), width=1)
plt.show()


# bar width를 매우 두껍게 하면?
plt.bar(range(1, 101), range(1, 101), width=10)
plt.show()


# bar width를 매우 가늘게 하면?
plt.bar(range(1, 101), range(1, 101), width=.1)
plt.show()


# bar width를 다양하게 바꿔가며 테스트
# colab과 vscode에서 그래프가 다르게 나올 수 있음
fig, ax = plt.subplots(1, 4, figsize=(15, 5))
widths = [.1, .2, .3, .4]
for i, w in enumerate(widths):
    ax[i].bar(range(100), range(100), width=w)
plt.show()


# 해결책: Figure 폭을 넓히고 bar width를 조절한다
plt.figure(figsize=(10, 4))
plt.bar(range(1, 101), range(1, 101), width=0.6)
plt.show()


# bar가 너무 많으면 Figure 폭으로도 해결되지 않을 수 있음
plt.bar(range(1000), range(1000))
plt.show()


# bar가 너무 많으면 bar width로도 해결되지 않을 수 있음
plt.bar(range(1000), range(1000), width=0.4)
plt.show()
