#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang
"""
希尔排序（shell sort）
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本,该方法的基本思想是：
先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，然后依次缩减增量再进行排序，
待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率比直接插入排序有较大提高
"""

import time,random

#source = [8, 6, 4, 9, 7, 3, 2, -4, 0, -100, 99]
#source = [92, 77, 8,67, 6, 84, 55, 85, 43, 67]

source = [ random.randrange(10000+i) for i in range(10000)]
#print(source)



step = int(len(source)/2) #分组步长

t_start = time.time()


while step >0:
    print("---step ---", step)
    #对分组数据进行插入排序

    for index in range(0,len(source)):
        if index + step < len(source):
            current_val = source[index] #先记下来每次大循环走到的第几个元素的值
            if current_val > source[index+step]: #switch
                source[index], source[index+step] = source[index+step], source[index]

    step = int(step/2)
else: #把基本排序好的数据再进行一次插入排序就好了
    for index in range(1, len(source)):
        current_val = source[index]  # 先记下来每次大循环走到的第几个元素的值
        position = index

        while position > 0 and source[
                    position - 1] > current_val:  # 当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
            source[position] = source[position - 1]  # 把左边的一个元素往右移一位
            position -= 1  # 只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止

        source[position] = current_val  # 已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
    print(source)

t_end = time.time() - t_start

print("cost:",t_end)