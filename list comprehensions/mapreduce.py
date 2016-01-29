# encoding=utf-8
# 高级函数
def f(x):
	return x * x

L=map(f, [1, 2, 3, 4, 5, 6, 7])
print L
print(map(str,[1,2,3,4,5,6]))
# reduce
def add(x, y):
	return x+y
print reduce(add, [1, 2, 3, 4])
# filter
def is_old(s):
	return s%2==1
print filter(is_old,[1,2,3,4,5,6,7,8,9])