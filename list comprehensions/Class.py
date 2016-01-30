#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""class 访问限制 类和实例 继承和多态"""

__author__ = "Jack MU"


class Student(object):  # 访问限制，类和实例

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError("bad score")


#  继承和多态
class Animal(object):
	def run(self):
		print "Animal is running..."


class Dog(Animal):
	def run(self):
		print "Dog is running..."


class Cat(Animal):
	def run(self):
		print "Cat is running..."

# 实例化调用
dog = Dog()
dog.run()
cat = Cat()
cat.run() #继承获得了父类的方法，有了自己的run方法后调用自己的run：多态


def run_twice(animal): 	# 测试多态
	animal.run()
	animal.run()


run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
	def run(self):
		print "Tortiose is running slowly"

run_twice(Tortoise())
