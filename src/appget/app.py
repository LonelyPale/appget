from abc import ABC, abstractmethod


class App(ABC):
    def __init__(self):
        if self.__class__ is App:
            # 如果试图直接实例化基类，则抛出错误
            raise NotImplementedError('Cannot instantiate Base Class <App> directly')
        self.__check_required_attribute()

    def __check_required_attribute(self):
        for key in ['name', 'version', 'desc', 'homepage', 'license']:
            if not hasattr(self, key):
                # 检查子类是否实现了必需的属性，子类的属性必须在调用父类的__init__方法前初始化
                raise NotImplementedError(f'Subclasses must set "{key}"')

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def uninstall(self):
        pass
