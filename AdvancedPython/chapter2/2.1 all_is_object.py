# 类与函数都是对象

def ask(name="ls"):
    print(name)


class Person:
    def __init__(self):
        print("lsls")

def print_type(item):
    print_type(type(item))


def decorator_func():
    print("dec start")
    return ask
# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())
# # my_func = ask
# # my_func()
#
#
# my_class = Person
# my_class()

my_ask = decorator_func()
my_ask("tom")
