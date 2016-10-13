#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang
"""
设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，
这个过程称为一趟快速排序。值得注意的是，快速排序不是一种稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动　　
注：在待排序的文件中，若存在多个关键字相同的记录，经过排序后这些具有相同关键字的记录之间的相对次序保持不变，该排序方法是稳定的；
若具有相同关键字的记录之间的相对次序发生改变，则称这种排序方法是不稳定的。
要注意的是，排序算法的稳定性是针对所有输入实例而言的。即在所有可能的输入实例中，只要有一个实例使得算法不满足稳定性要求，则该排序算法就是不稳定的。
"""

def quick_sort(array,left,right):
    '''

    :param array:
    :param left: 列表的第一个索引
    :param right: 列表最后一个元素的索引
    :return:
    '''
    if left >=right:
        return
    low = left
    high = right
    key = array[low] #第一个值

    while low < high:#只要左右未遇见
        while low < high and array[high] > key: #找到列表右边比key大的值 为止
            high -= 1
        #此时直接 把key(array[low]) 跟 比它大的array[high]进行交换
        array[low] = array[high]
        array[high] = key


        while low < high and array[low] <= key : #找到key左边比key大的值，这里为何是<=而不是<呢？你要思考。。。
            low += 1
            #array[low] =
        #找到了左边比k大的值 ,把array[high](此时应该刚存成了key) 跟这个比key大的array[low]进行调换
        array[high] = array[low]
        array[low] = key

    quick_sort(array,left,low-1) #最后用同样的方式对分出来的左边的小组进行同上的做法
    quick_sort(array,low+1, right)#用同样的方式对分出来的右边的小组进行同上的做法



if __name__ == '__main__':

    array = [96,14,10,9,6,99,16,5,1,3,2,4,1,13,26,18,2,45,34,23,1,7,3,22,19,2]
    #array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
    print("before sort:", array)
    quick_sort(array,0,len(array)-1)

    print("-------final -------")
    print(array)