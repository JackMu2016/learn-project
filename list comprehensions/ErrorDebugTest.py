#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import logging
"""错误粗粒"""

__author__ = "JackMu"


# 错误处理
# print int("a")
try:
	print "try..."
	r = 10 / 2
	print "result:", r
except ZeroDivisionError, e:
	print "except:", e
finally:
	print "finally..."
print "END"

# 多种错误类型
try:
	print "try..."
	r = 10 / int('a')
	print "result:", r
except ValueError, e:
	print "ValueError:", e
except ZeroDivisionError, e:
	print "ZeroDivisionError:", e
else:  # 无错误还能执行else后面的语句
	print "no error!"
finally:
	print "finally..."
print "END"


# 没有被捕获会一直上抛至err.py
#err.py
def foo(s):
	return 10 / int(s)


def bar(s):
	return foo(s) * 2


def main():
	bar('0')

# main()


# 记录错误
def foo2(s):
	return 10 / int(s)


def bar2(s):
	return foo2(s) * 2


def main2():
	try:
		bar2("0")
	except StandardError, x:
		logging.exception(x)


main2()
print "end"
