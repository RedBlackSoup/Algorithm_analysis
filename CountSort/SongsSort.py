# -*- coding: utf-8 -*-
import jieba
import matplotlib.pyplot as plt
from matplotlib.pylab import style


def wordsort(path):
    txt = open(path, "r", encoding='utf-8').read()
    words = jieba.lcut(txt)  # 使用精确模式对文本进行分词
    counts = {}  # 通过键值对的形式存储词语及其出现的次数
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            # 遍历所有词语，每出现一次其对应的值加 1
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    # 根据词语出现的次数进行从大到小排序
    items.sort(key=lambda x: x[1], reverse=True)
    # for i in range(10):
    #      word, count = items[i]
    #      print("{0:<5}{1:>5}".format(word, count))
    return items


# 歌词集路径
path_wf = 'wf.txt'
path_zj = 'zj.txt'
# 分词集以及词频
word_wf = []
counts_wf = []
word_zj = []
counts_zj = []
# 分别进行分词
item1 = wordsort(path_wf)
item2 = wordsort(path_zj)
# 统计频率前10的歌词
for i in range(10):
    word_wf.append(item1[i][0])
    counts_wf.append(item1[i][1])
    print("{0:<5}{1:>5}".format(item1[i][0], item1[i][1]))
print("*"*50)
for i in range(10):
    word_zj.append(item2[i][0])
    counts_zj.append(item2[i][1])
    print("{0:<5}{1:>5}".format(item2[i][0], item2[i][1]))
# 设置图表样式
style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 绘制结果
plt.title('郑钧汪峰歌词统计')
plt.bar(word_wf, counts_wf, label='汪峰')
plt.legend()
plt.show()
plt.title('郑钧汪峰歌词统计')
plt.bar(word_zj, counts_zj, color='g', label='郑钧')
plt.legend()
plt.show()
