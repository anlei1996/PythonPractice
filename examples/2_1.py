# 目标：如何在列表，字典，集合中根据条件筛选数据
from random import randint
from time import time as time


# 自定义函数，筛选出大于等于0的元素
def fun1(data):
    new_data = []
    for x in data:
        if x >= 0:
            new_data.append(x)
    return new_data


# 运用filter函数，筛选出大于等于0的元素
def fun2(data):
    new_data = list(filter(lambda x: x >= 0, data))  # filter在py2与py3中不同
    return new_data


# 在列表中，运用列表解析，筛选出大于等于0的元素， 比filter速度快1倍
def fun3(data):
    new_data = [x for x in data if x >= 0]
    return new_data


#  在字典中,运用字典解析，筛选出值大于90的元素
def fun4():
    data = {x: randint(60, 100) for x in range(10)}
    new_data = {k: v for k, v in data.items() if v > 90}
    return new_data


# 在集合中，运用集合解析，筛选出能被3整除的元素
def fun5(data):
    new_data = {x for x in data if x % 3 == 0}
    return new_data


if __name__ == "__main__":

    # 准备数据
    data = [1, 5, -3, -2, 6, 0, 9, 1]
    print("初始数据为：", data)
    print("---------------------------------------")

    # 测试每个函数
    t1 = fun1(data)
    print("自定义函数：", t1)
    t2 = fun2(data)
    print("使用filter函数函数：", t2)
    t3 = fun3(data)
    print("使用列表解析：", t3)
    t4 = fun4()
    print("使用字典解析：", t4)
    t5 = fun5(set(data))
    print("使用集合解析：", t5)

    # 测试filter函数与列表解析的速度差异
    start1 = time()
    for i in range(10000):  # 测试filter函数的速度
        fun2(data)
    end1 = time()
    time1 = end1 - start1
    print("filter函数运行1000次的时间为：", time1)

    start2 = time()
    for i in range(10000):  # 测试filter函数的速度
        fun3(data)
    end2 = time()
    time2 = end2 - start1
    print("列表解析运行1000次的时间为：", time2)
    print("time1/time2 = ", time1 / time2)
    # 时间到底哪个快？
