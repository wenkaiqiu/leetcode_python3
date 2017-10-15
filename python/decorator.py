def logging_decorator(func):
    count = 0

    def wrapper():
        wrapper.count += 1
        print("local count = %d" % count)  # 虽然报错，但可运行,不可修改
        print("The function I modify has been called {0} times(s).".format(wrapper.count))
        func()

    wrapper.count = 0  # 在Python中, 闭包完整的提供了对方法作用域链中变量的读权限，但只为同样作用域中的可变对象(比如, 列表, 字典等)提供了写权限
    return wrapper


def a_function():
    print("I'm a normal function.")


modified_function = logging_decorator(a_function)

modified_function()
modified_function()
modified_function()
