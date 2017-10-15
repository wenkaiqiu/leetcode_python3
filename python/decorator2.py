import sys

"""
    结论：装饰器在类__init__前调用，且其可被继承
"""
def decorator():
    print("----1----")
    frame = sys._current_frames()
    frame2 = sys._getframe()
    print(frame)
    print("----3----")
    print(frame2)
    def print2(Test):
        print("abc")
        return Test
    return print2

@decorator()
class Test:
    def __new__(cls, *args, **kwargs):
        print("aaaa")
        # cls.id = 1
        # print(cls.id)
        return object.__new__(cls)

    def __init__(self):
        print("---2----")
        frame = sys._current_frames()
        frame2 = sys._getframe()
        print(frame)
        print(frame2)


class B(Test):
    def __new__(cls, *args, **kwargs):
        print("bbbb")
        # print(cls.id)
        # return Test.__new__(cls, args, kwargs)
        # return cls.__new__(cls, args, kwargs)

    def __init__(self):
        super().__init__()
        print("----4-----")


if __name__ == "__main__":
    B()
