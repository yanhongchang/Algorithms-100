#Author: jourminyan
# -*- coding:utf-8 -*-

# 【选择排序】
# 最常见的排序算法之一
# 遍历列表，找到最小的元素，与列表第一个元素交换，然后继续遍历剩余的列表，核心是元素交换
# 时间复杂度：O(n2), 空间复杂度：O(1)

slist = [10, 6, 101, 2, 4, 12, 100]


def choice_sort(slist):
    for i in range(0, len(slist)):
        print '----%s----' % i
        min_loc = i
        for j in range(i+1, len(slist)):
            if slist[min_loc] > slist[j]:
                min_loc = j
        slist[i], slist[min_loc] = slist[min_loc], slist[i]
        print slist
    return slist

choice_sort(slist)