import os
import platform

LINUX = 'linux'
DARWIN = 'darwin'
WINDOWS = 'windows'

OS = platform.system().lower()
ARCH = platform.machine().lower()

SHELL = os.getenv('SHELL')
HOME = os.getenv('HOME')


def is_linux() -> bool:
    return OS == LINUX


def is_darwin() -> bool:
    return OS == DARWIN


def is_windows() -> bool:
    return OS == WINDOWS


def is_root():
    # 在Unix-like系统中，root用户的用户ID通常为0。
    return os.geteuid() == 0
