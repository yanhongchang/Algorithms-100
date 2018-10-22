#Author: jourminyan
# -*- coding:utf-8 -*-

# 【二分查询】or 【折半查找】
# 适用于已经有序的列表进行查找
# 找到后返回元素下标，否则返回"Not find"
# 时间复杂度：O(nlogn), 空间复杂度：O(1)

sear_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 10


def bin_search(slist, ele):
    low = 0
    high = len(slist) - 1

    while low <= high:
        mid_loc = (low + high) / 2
        if ele == slist[mid_loc]:
            return mid_loc
        elif ele < slist[mid_loc]:
            high = mid_loc - 1
        else:
            low = mid_loc + 1
    return None


re = bin_search(sear_list, element)
if re:
    print re
else:
    print "Not find the ele: {0}".format(element)

