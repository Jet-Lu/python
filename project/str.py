# -*- coding: utf-8 -*-

print('包含中文的str')
print(ord('A'))
a = b'ABC'.decode('ascii')
print(a)

print('%2d-%02d' % (3,1))
print('%.2f' % 3.14)
b = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print(b)

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明成绩提升了%.1f%%' %r)

# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michae', 'Bob', 'Tracy']
classmates.append('Jet Lu')
print('1', classmates)
classmates.insert(1, 'Jet Li')
print('2', classmates)

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
t = ('a', 'b', ['A', 'B'])


age = 10
if age >= 18:
	print('your age is', age)
	print('adult')
else:
	print('your age is', age)
	print('teenager')

