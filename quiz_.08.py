#python字典和json字符串相互转化方法
import json

# 将字典转为 JSON 字符串
data = {
    "name": "Tom",
    "age": 18,
    "city": "Beijing"
}
json_str = json.dumps(data)
print("字典转换为 JSON 字符串：", json_str)

# 将 JSON 字符串转为字典
data_again = json.loads(json_str)
print("JSON 字符串转换为字典：", data_again)