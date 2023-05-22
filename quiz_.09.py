#递归求和
def sum_list_recursive(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list_recursive(lst[1:])

# 测试代码
nums = [5, 6, 7, 8, 9]
result = sum_list_recursive(nums)
print(result)