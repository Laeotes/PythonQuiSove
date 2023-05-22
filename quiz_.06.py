#求两个列表的交集、差集、并集
# 定义两个列表
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# 求交集
intersection = list(set(list1).intersection(set(list2)))
print("交集：", intersection)

# 求差集
difference = list(set(list1).difference(set(list2)))
print("差集：", difference)

# 求并集
union = list(set(list1).union(set(list2)))
print("并集：", union)