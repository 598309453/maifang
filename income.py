# 买房程序v3.0.1 输入每月存款金额进行保存
from matplotlib import pyplot
from pylab import mpl


def save_income():
    data = []
    for i in range(1, 5):
        income = float(input("请输入存款金额:"))
        # 将金额放入列表中
        data.append(income)
    return data


def graphic_income(month, income):
    mpl.rcParams['font.sans-serif'] = ['FangSong']

    pyplot.xlabel("月份")
    pyplot.ylabel("存款金额")
    pyplot.title("存款统计图表")

    pyplot.yticks([0, 1000, 2000, 3000, 4000])
    pyplot.xticks([1, 2, 3, 4, 5])
    pyplot.plot(month, income)
    pyplot.show()


month = [1, 2, 3, 4]
# income = []
income = save_income()
# print(month)
# print(income)

graphic_income(month, income)
