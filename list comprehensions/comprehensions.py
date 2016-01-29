import os
# coding=utf-8
# 列表生产式
# 1x1, 2x2, 3x3, ..., 10x10
s = [x*x for x in range(1, 10)]
print(s)
s = [x*x for x in range(1, 10) if x % 2 == 0]
print(s)
print([m + n for m in "abc" for n in "123"])

# 列出当前目前下所有文件和目录名
print([d for d in os.listdir("d:/")])
# for 可以同时使用多个变量
d = {'a ': 'a', "c": "cd"}
print([ k+"="+v for k,v in d.iteritems()])

L = ["hELLO", "World", "IBN"]
print([s.lower() for s in L])

