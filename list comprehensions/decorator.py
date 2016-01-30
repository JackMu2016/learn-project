# encoding=utf-8
import functools


def now():
	print("2016-1-30")


f = now
print(f())
print(now.__name__)
print(f.__name__)


def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)

	return wrapper


@log
def now1():
	print "2016-01-30"
print(now1())

#标准定义


def log2(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)

	return wrapper


@log2
def now2():
	print "2016-01-30 now2"

print(now2())


# 带参数的decorator
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s()' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator


@log("execute")
def now3():
	print "2016---"
print now3()


# 偏函数:把一个函数的某些参数给固定住（也就是设置默认值）
# 返回一个新的函数
int2 = functools.partial(int, base=2)
print(int2("1000000"))
print(int2("1010101"))
# 默认值也可在调用时传入其他值
print(int2("1000000", base=10))





