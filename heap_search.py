#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang

"""
堆排序，顾名思义，就是基于堆。因此先来介绍一下堆的概念。
堆分为最大堆和最小堆，其实就是完全二叉树。最大堆要求节点的元素都要大于其孩子，最小堆要求节点元素都小于其左右孩子，两者对左右孩子的大小关系不做任何要求，
其实很好理解。有了上面的定义，我们可以得知，处于最大堆的根节点的元素一定是这个堆中的最大值。
其实我们的堆排序算法就是抓住了堆的这一特点，每次都取堆顶的元素，将其放在序列最后面，然后将剩余的元素重新调整为最大堆，依次类推，最终得到排序的序列。
"""
"""
人类能理解的版本
"""
dataset = [16,9,21,3,13,14,23,6,4,11,3,15,99,8,22]

for i in range(len(dataset)-1,0,-1):
    print("-------",dataset[0:i+1],len(dataset),i)
    #for index in range(int(len(dataset)/2),0,-1):
    for index in range(int((i+1)/2),0,-1):
        print(index)
        p_index = index

        l_child_index = p_index *2 - 1
        r_child_index = p_index *2
        print("l index",l_child_index,'r index',r_child_index)
        p_node = dataset[p_index-1]
        left_child =  dataset[l_child_index]

        if p_node < left_child:  # switch p_node with  left child
            dataset[p_index - 1], dataset[l_child_index] = left_child, p_node
            # redefine p_node after the switch ,need call this val below
            p_node = dataset[p_index - 1]

        if r_child_index < len(dataset[0:i+1]): #avoid right out of list index range
        #if r_child_index < len(dataset[0:i]): #avoid right out of list index range
            #print(left_child)
            right_child =  dataset[r_child_index]
            print(p_index,p_node,left_child,right_child)

            # if p_node <  left_child: #switch p_node with  left child
            #     dataset[p_index - 1] , dataset[l_child_index] = left_child,p_node
            #     # redefine p_node after the switch ,need call this val below
            #     p_node = dataset[p_index - 1]
            #
            if p_node < right_child: #swith p_node with right child
                dataset[p_index - 1] , dataset[r_child_index] = right_child,p_node
                # redefine p_node after the switch ,need call this val below
                p_node = dataset[p_index - 1]

        else:
            print("p node [%s] has no right child" % p_node)


    #最后这个列表的第一值就是最大堆的值，把这个最大值放到列表最后一个， 把神剩余的列表再调整为最大堆

    print("switch i index", i, dataset[0], dataset[i] )
    print("before switch",dataset[0:i+1])
    dataset[0],dataset[i] = dataset[i],dataset[0]
    print(dataset)

