# decorator for functions in class
#定义一个装饰类
class DeracotorClass:

    def deracotor1(self,func): # 因为该装饰方法是定义在类中所以这里需要加一个self

        def inner(self, *args, **kwargs):
            print('开始装饰1')
            import re
            str = r"[^@]+@[^@]+\.[^@]+"
            if re.match(str, args[0]):
                print('邮箱格式正确')
                res = func(self,*args,**kwargs)
            else:
                print('邮箱格式错误')
                res = None
            print('结束装饰1')
            return res
        return inner

    def deracotor2(func): # 使用func代替self，调用时需使用类名调用

        def inner(self,*args,**kwargs):
            print('开始装饰2')
            if args[0] > 10:
                print('a大于10')
                res = None
            elif args[1] < 100:
                print('b小于100')
                res = None
            else:
                res = func(self,*args,**kwargs)
            print('结束装饰2')
            return res
        return inner


    @staticmethod
    def static_deracotor(func):  # 静态方法
        def inner(self):
            print('开始装饰3')
            func(self)
            print('结束装束3')
        return inner

    @classmethod
    def class_deracotor(cls,func):  #类方法带有cls参数
        def inner(self):
            print('开始装饰4')
            func(self)
            print('结束装饰4')
        return inner

c = DeracotorClass() # 为了使用类中第一个装饰方法在这里需创建一个对象

class People:
    @c.deracotor1 # 使用类中的实例方法装饰
    def my_func1(self,email):
        print('联系人邮箱：',email)
        print('my_func1')

    @DeracotorClass.deracotor2  # 需要直接使用类名调用
    def my_func2(self, a, b):
        print(f'a = {a}, b = {b}')
        c = a + b
        print(f'总数{c}超过100' if c > 100 else f'总数{c}不超过100')

    @DeracotorClass.static_deracotor # 使用装饰类中定义的静态装饰方法
    def my_func3(self):
        print('my_func3')

    @DeracotorClass.class_deracotor  # 使用装饰类中的定义的类装饰方法
    def my_func4(self):
        print('my_func4')

#创建一个对象
p = People()

# 调用实例方法
p.my_func1('asfasf@sadf.csaf')
p.my_func2(0,110)
p.my_func3()
p.my_func4()
