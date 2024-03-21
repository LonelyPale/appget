import os
import sys
import inspect

from abc import ABC, abstractmethod

from appget import log
from appget.utils import DEBUG


class App(ABC):
    __required_attributes = ['name', 'version', 'desc', 'homepage', 'license']

    def __init__(self):
        if self.__class__ is App:
            # 如果试图直接实例化基类，则抛出错误
            raise NotImplementedError('Cannot instantiate Base Class <App> directly')
        self.__check_required_attribute()

    def __check_required_attribute(self):
        for key in self.__required_attributes:
            if not hasattr(self, key):
                # 检查子类是否实现了必需的属性，子类的属性必须在调用父类的__init__方法前初始化
                raise NotImplementedError(f'Subclasses must set "{key}"')

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def uninstall(self):
        pass

    def info(self):
        for key in self.__required_attributes:
            if hasattr(self, key):
                log.info(f'{key.capitalize()}: {getattr(self, key)}')

        if DEBUG:
            module_name = self.__module__
            module_object = sys.modules[module_name]
            module_file = module_object.__file__
            module_path = os.path.dirname(module_file)
            run_name = f'{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}'
            log.debug(f'{run_name}: module_name={module_name}')
            log.debug(f'{run_name}: module_path={module_path}')
            log.debug(f'{run_name}: module_object={module_object}')
