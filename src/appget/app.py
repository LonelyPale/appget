import os.path
import sys
import inspect
import shutil

from abc import ABC, abstractmethod

from appget import log, profile
from appget.constant import *
from appget.utils import copy_file_or_folder


class App(ABC):
    __required_attributes = ['name', 'version', 'desc', 'license', 'homepage']
    __info_attributes = ['name', 'version', 'desc', 'license', 'homepage', 'homepath']

    def __init__(self):
        if self.__class__ is App:
            # 如果试图直接实例化基类，则抛出错误
            raise NotImplementedError('Cannot instantiate Base Class <App> directly')
        self.__check_required_attribute()
        self.home_path = os.path.join(APP_HOME, getattr(self, 'name'))
        self.install_path = os.path.join(self.home_path, getattr(self, 'version'))
        self.bin_path = os.path.join(self.install_path, 'bin')
        self.script_name, self.script_path = self.__script_name_and_path()

    def __check_required_attribute(self):
        for key in self.__required_attributes:
            if not hasattr(self, key):
                # 检查子类是否实现了必需的属性，子类的属性必须在调用父类的__init__方法前初始化
                raise NotImplementedError(f'Subclasses must set "{key}"')
            if key == 'name' and getattr(self, key) == '':
                raise NotImplementedError(f'Subclasses must set "{key}" and non-empty')
            if key == 'version' and getattr(self, key) == '':
                raise NotImplementedError(f'Subclasses must set "{key}" and non-empty')

    @abstractmethod
    def install(self):
        target_path = f'{self.home_path}/.appget'
        copy_file_or_folder(self.script_path, target_path)

    @abstractmethod
    def uninstall(self):
        appname = getattr(self, 'name')
        if self.home_path.endswith(appname):
            shutil.rmtree(self.home_path)
        else:
            log.error(f'Invalid homepath: appname={appname} homepath={self.home_path}')

    def info(self):
        self.__display_attributes(self.__info_attributes)

    def search(self):
        self.__display_attributes(self.__required_attributes)

    def __display_attributes(self, attributes):
        for key in attributes:
            log.info(f'{key.capitalize()}: {getattr(self, key)}')

        if DEBUG:
            run_name = f'{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}'
            module = sys.modules[self.__module__]
            log.debug(f'{run_name}: module={module}')

    def __script_name_and_path(self):
        module_name = self.__module__
        module = sys.modules[module_name]
        module_file = module.__file__
        script_name = os.path.basename(module_file)[:-3]
        return script_name, module_file

    def add_profile(self, content):
        """添加 app script 到 .profile 文件"""
        if content == '':
            return
        appname = getattr(self, 'name')
        profile.app_profile_install(appname, content)

    def del_profile(self):
        """从 .profile 文件删除 app script"""
        appname = getattr(self, 'name')
        profile.app_profile_uninstall(appname)

    def copy_bin(self, source, is_create_link=True):
        if not os.path.isfile(source):
            log.warning(f'not a file: {source}')
            return

        if not os.path.exists(self.bin_path):
            os.makedirs(self.bin_path)

        basename = os.path.basename(source)
        dest = os.path.join(self.bin_path, basename)
        shutil.copy2(source, dest)

        if is_create_link:
            symlink_path = os.path.join(BIN_HOME, basename)
            os.symlink(dest, symlink_path)

