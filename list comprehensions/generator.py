# encoding=utf-8
L=[x*x for x in range(1,10)]
print(L)
L2=(x*x for x in range(1,10))  # 生成器 推算
print L2.next()  # 打印方法1
print L2.next()
# 方法2
for n in L2:
	print n


# 打印斐波拉契数列 复杂推算
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n+=1


for n in fib(6):
	print(n)
