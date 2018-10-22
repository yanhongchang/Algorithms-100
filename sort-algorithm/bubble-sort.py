#Author: jourminyan
# -*- coding:utf-8 -*-

# 【冒泡排序】
# 最常见的排序算法之一
# 时间复杂度：O(n2), 空间复杂度：O(1)

slist = [10, 6, 10, 101, 2, 4, 12, 100]


def bubble_sort(slist):
    high = len(slist)-1
    for j in range(high, 0, -1):
        for i in range(0, high):
            if slist[i] > slist[i+1]:
               slist[i], slist[i+1] = slist[i+1], slist[i]
    return slist


def bubble_sort_new(slist):
    high = len(slist)-1
    for i in range(high, 0, -1):
        exchange = False
        for j in range(0, i):
            if slist[j] > slist[j+1]:
                slist[j], slist[j+1] = slist[j+1], slist[j]
                exchange = True
        if not exchange:
            return slist


print bubble_sort_new(slist)

