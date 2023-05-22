#利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter

str1 = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
word_count = Counter(str1.split(';'))

print(word_count)
