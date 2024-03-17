class MyBaseClass:
    def __init__(self):
        if self.__class__ is MyBaseClass:
            # 如果试图直接实例化基类，则抛出错误
            raise NotImplementedError("Cannot instantiate MyBaseClass directly")
        # 检查子类是否实现了必需的属性
        if not hasattr(self, 'required_attribute'):
            raise NotImplementedError("Subclasses must set 'required_attribute'")


class MySubClass(MyBaseClass):
    def __init__(self, required_attribute):
        # 调用父类的初始化方法
        self.required_attribute = required_attribute
        super().__init__()


# 试图实例化基类会抛出错误
# try:
#     base = MyBaseClass()
# except NotImplementedError as e:
#     print(e)


if __name__ == '__main__':
    # 实例化子类时必须提供必需的属性值
    try:
        sub = MySubClass("some_value")
        print("Subclass instantiated successfully!")
    except NotImplementedError as e:
        print(e)
