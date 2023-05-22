#正则匹配不是以4和7结尾的手机号
import re

phone_numbers = [
    "13800010002",
    "13800010004",
    "13800010009",
    "13800010072",
    "13800010077",
    "13800010071",
]

pattern = re.compile("^1\d{9}(?<![47])$")

for phone in phone_numbers:
    match = pattern.match(phone)
    if match:
        print("匹配成功：", phone)
    else:
        print("匹配失败：", phone)