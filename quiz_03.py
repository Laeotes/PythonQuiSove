#列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# 原始列表
lst = [1, 2, 3, 4, 5]

# 使用 map() 函数求平方
squared_lst = list(map(lambda x: x ** 2, lst))
print(squared_lst)

# 列表推导式提取大于 10 的数
filtered_lst = [x for x in squared_lst if x > 10]
print(filtered_lst)