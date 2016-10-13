#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


"""
The algorithm works by selecting the smallest unsorted item and then swapping it with the item in the next position to be filled.

The selection sort works as follows: you look through the entire array for the smallest element, once you find it you swap it
(the smallest element) with the first element of the array. Then you look for the smallest element in the remaining array
 (an array without the first element) and swap it with the second element. Then you look for the smallest element in the remaining array
 (an array without first and second elements) and swap it with the third element, and so on. Here is an example,
 The worst-case runtime complexity is O(n2).　
"""

data_set = [ 9,1,22,31,45,3,6,2,11 ]

smallest_num_index = 0 #初始列表最小值,默认为第一个

loop_count = 0
for j in range(len(data_set)):
    for i in range(j,len(data_set)):
        if data_set[i] < data_set[smallest_num_index]: #当前值 比之前选出来的最小值 还要小,那就把它换成最小值
            smallest_num_index = i
        loop_count +=1
    else:
        print("smallest num is ",data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] =  data_set[j]
        data_set[j] = tmp

    print(data_set)
    print("loop times", loop_count)



"""
data_set = [ 9,1,22,9,31,-5,45,3,6,2,11 ]
for i in range(len(data_set)):
    #position  = i
    while i > 0 and data_set[i] < data_set[i-1]:# 右边小于左边相邻的值
        tmp = data_set[i]
        data_set[i] = data_set[i-1]
        data_set[i-1] = tmp
        i -= 1
    # position  = i
    # while position > 0 and data_set[position] < data_set[position-1]:# 右边小于左边相邻的值
    #     tmp = data_set[position]
    #     data_set[position] = data_set[position-1]
    #     data_set[position-1] = tmp
    #     position -= 1

插入排序
"""