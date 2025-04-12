# -*- coding: UTF-8 -*-

# filename : test_function_params.py
# description : 函数参数之位置参数，可变参数，关键字参数，默认参数，命名关键字参数
# author by : peanut
# date : 2025/4/12


"""
    位置参数与可变参数
"""


def hello(greeting, *args):
    if len(args) == 0:
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


# => greeting='Hi', args=()
hello('Hi')

# => greeting='Hi', args=('Sarah')
hello('Hi', 'Sarah')

# => greeting='Hello', args=('Michael', 'Bob', 'Adam')
hello('Hello', 'Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
# => greeting='Hello', args=('Bart', 'Lisa')
hello('Hello', *names)


"""
    关键字参数
"""


def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

"""
    命名关键字参数 只接受*后面的参数座位关键字参数
"""


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)