#python中生成随机整数、随机小数、0--1之间小数方法
#生成随机整数可以使用random模块下的randint()函数，它接收两个参数，返回一个范围内的随机整数
import random

# 生成1到100的随机整数
rand_int = random.randint(1, 100)
print(rand_int)
#生成随机小数可以使用random模块下的uniform()函数，它接收两个参数，返回一个范围内的随机小数
import random

# 生成1.0到10.0的随机小数
rand_float = random.uniform(1.0, 10.0)
print(rand_float)
#生成0到1之间的随机小数可以使用random模块下的random()函数
import random

# 生成0到1之间的随机小数
rand_zero_one = random.random()
print(rand_zero_one)