# -*- coding: UTF-8 -*-

# filename : test_collections.py
# description : 使用collections
# author by : peanut
# date : 2025/4/30

"""
    collections是Python内建的一个集合模块，提供了许多有用的集合类。
"""

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse


"""
    1. namedtuple
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
    这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
    可以验证创建的Point对象是tuple的一种子类：
"""

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

"""
    2. deque
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，
    数据量大的时候，插入和删除效率很低。
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
    这样就可以非常高效地往头部添加或删除元素。

"""

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

"""
    3. defaultdict
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict.
    defaultdict是dict的一个子类，它默认的value是一个工厂函数，当key不存在时，
    返回的是工厂函数的默认值，比如list、set、或者int。

"""

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
if dd['key2'] == 'N/A':
    print('key2 does not exist')

"""
    4. OrderedDict
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    如果要保持Key的顺序，可以用OrderedDict。
    OrderedDict的key会按照插入的顺序排列，不是key本身排序。
    OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
"""

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

"""
    5. ChainMap
    ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是它用list存储了多个dict，
    然后，按顺序在list中依次查找key。
    什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，
    可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，
    再查环境变量，如果没有，就使用默认参数。
    
"""


# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


"""
    6. Counter
    Counter是一个简单的计数器，例如，统计字符出现的个数。
    Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数。
"""

c = Counter()
print(c)
c = Counter('programming')
print(c)
c = Counter({'red': 4, 'blue': 2})
print(c)










