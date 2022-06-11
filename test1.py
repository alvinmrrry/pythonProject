def dec(func):
    def inner(*args, **kwargs):
        print('before')
        res = func(*args, **kwargs)
        print('after')
        return res
    return inner

@dec
def add(a, b):
    return a + b

print(add(1, 2))
print(add(3,5))


# 带参数的类装饰器
class dec2(object):
    def __init__(self, flag):
        self.flag = flag

    def __call__(self, func):
        def inner(*args, **kwargs):
            if self.flag:
                print('before')
            res = func(*args, **kwargs)
            if self.flag:
                print('after')
            return res
        return inner

@dec2(flag=True)
def add2(a, b):
    return a + b

add2(1, 2)
    


