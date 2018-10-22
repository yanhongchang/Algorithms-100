#Author: jourminyan
# -*- coding:utf-8 -*-

# 【列表查询】
# 普通的列表查找，找到后返回元素下标，否则返回"Notfind"
# 时间复杂度：O(n), 空间复杂度：O(1)

sear_list = [10, 3, 6, 10, 101, 2, 4, 12, 18]
element = 7


def ord_search(slist, ele):
    for i in range(0, len(slist)):
        if ele == slist[i]:
            return i
    return None


re = ord_search(sear_list, element)
if re:
    print re
else:
    print "Not find the ele: %s" % element
