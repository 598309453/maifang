# v1.0 买房子
# 输入相关数据
# price = int(input("请输入房价："))
# area = int(input("你想住多大的房子："))
# year = int(input("你想几年内买房："))
# consume = float(input("你每月的额定消费是："))
# income = format((price * area * 0.3) / (year*12) + consume,".2f")
# print("我们目标应每月收入: ", income)

# v2.0 买房子
import csv


def get_price(city_price):
    # 读取房价文件
    file = open("price.csv", "r")
    table = csv.reader(file)
    for row in table:
        if city_price == row[0]:
            return row[1]


def save_result(city_result, area_result, year_result, income_result):
    file = open("aim.csv", "w")
    file.write("城市" + "," + city_result)
    file.write(",")
    file.write("面积" + "," + str(area_result))
    file.write(",")
    file.write("年限" + "," + str(year_result))
    file.write(",")
    file.write("月收入"+","+ str(income_result))
    file.close()


city = str(input("请输入你想定居的城市："))
price = int(get_price(city))
area = int(input("你想住多大的房子："))
year = int(input("你想几年内买房："))
consume = float(input("你每月的额定消费是："))
income = format((price * area * 0.3) / (year * 12) + consume, ".2f")
print("我们目标应每月收入: ", income)
save_result(city, area, year, income)
