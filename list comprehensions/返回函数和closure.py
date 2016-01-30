# encoding=utf-8
# 返回函数&闭包 closure

#普通求和函数


def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax


#调用
print calc_sum(*(1, 2, 3, 4))


#返回函数
def lazy_sum(*args):
	def su():
		az = 0
		for n in args:
			az = az + n
		return az

	return su


f = lazy_sum(*(1, 2, 3, 4, 5))

print(f)
print(f())  #调用f()才计算和
f2 = lazy_sum(*(1, 2, 3, 4, 5))
print(f == f2)
# False 两次调用互补影响

# 匿名函数
f = map(lambda x: x * x, [1, 2, 3, 4, 5, 6])
print(f)

fx = lambda x: x * x
# print(fx)


def build(x, y):
	return lambda: x * x + y * y
f = build(2, 4)
print(f)
