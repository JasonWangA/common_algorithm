#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang
"""
冒泡排序（Bubble Sort）
冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名。
"""

data_set = [9,1,22,31,45,3,6,2,11]


loop_count = 0
for j in range(len(data_set)):
    for i in range(len(data_set) -j - 1): # -1 是因为每次比对的都 是i 与i +1,不减1的话,最后一次对比会超出list 获取范围,-j是因为,每一次大loop就代表排序好了一个最大值,放在了列表最后面,下次loop就不用再运算已经排序好了的值 了
        if data_set[i] > data_set[i+1]: #switch
            tmp = data_set[i]
            data_set[i] = data_set[i+1]
            data_set[i+1] = tmp
        loop_count += 1

    print(data_set)
print(data_set)
print("loop items", loop_count)