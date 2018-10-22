#Author: jourminyan
# -*- coding:utf-8 -*-

# 【插入排序】
# 最常见的排序算法之一
#
# 时间复杂度：O(n2), 空间复杂度：O(1)

slist = [10, 6, 10, 101, 2, 4, 12, 100]

def insert_sort(slist):
    for i in range(1, len(slist)):
        temp = slist[i]
        for j in range(i-1, -1, -1):
            if slist[j] > temp:
                slist[j+1] = slist[j]
                slist[j] = temp
    return slist


print insert_sort(slist)