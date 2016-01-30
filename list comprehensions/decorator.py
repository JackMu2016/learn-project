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


