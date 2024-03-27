import os
import re
import shutil

from appget.constant import APP_PROFILE
from appget.system import is_linux, is_darwin

a = '''
. ~/.bash_profile

# start:lonely:go
# end:lonely:go

python读取~/.bash_profile文件，找到以'# app.profile#start'开始，以'# app.profile#end'结束的内容，把中间的内容替换为
```
abc
123
啊水电费
```
'''


# 在linux中，一般情况下.profile中会导入.bashrc，
# .bashrc是每次打开一个新的终端窗口（bash shell）时都会执行的文件。
# .profile是登录(login)时执行的文件，即当用户登录时会执行一次。
PROFILE_LINUX = ['~/.bashrc']

# .bash_profile文件是macOS系统中Bash shell的默认登录脚本。
PROFILE_DARWIN = ['~/.bash_profile']

TAG = '{appname}'
START = '# app.{appname}#start'
END = '# app.{appname}#end'
PATTERN = r'# app\.{appname}#start(.*?)# app\.{appname}#end'  # 正则表达式模式
PROFILE_LOAD_SCRIPT = f'[[ -s "{APP_PROFILE}" ]] && source "{APP_PROFILE}"'
PROFILE_TAG = 'profile'


def install_appget_profile_darwin():
    pass


def install_appget_profile(filepath):
    # 文件路径
    bash_profile_path = os.path.expanduser('~/.bash_profile')
    # 读取文件内容
    with open(bash_profile_path, 'r') as file:
        content = file.read()
    # 正则表达式模式
    pattern = r'# app\.profile#start(.*?)# app\.profile#end'
    # 新的内容
    new_content = '''abc
123
啊水电费
'''
    # 替换内容
    content, num_substitutions = re.subn(pattern, new_content, content, flags=re.DOTALL)
    # 如果有替换发生，写入文件
    if num_substitutions > 0:
        # with open(bash_profile_path, 'w') as file:
        #     file.write(content)
        print("文件已更新。")
    else:
        print("没有找到要替换的内容。")

    file_path = os.path.expanduser("~/.bash_profile")
    with open(file_path, 'r') as file:
        file_content = file.readlines()

    return


def get_profile_paths():
    if is_linux():
        return PROFILE_LINUX
    elif is_darwin():
        return PROFILE_DARWIN
    else:
        return []


def app_profile_install():
    pattern = PATTERN.replace(TAG, PROFILE_TAG)
    repl = PROFILE_LOAD_SCRIPT
    for filepath in get_profile_paths():
        update(filepath, pattern, repl)


def app_profile_uninstall():
    pattern = PATTERN.replace(TAG, PROFILE_TAG)
    repl = ''
    for filepath in get_profile_paths():
        update(filepath, pattern, repl, is_new=False)


def update(filepath, pattern, repl, is_new=True):
    """
    修改profile文件内容，更新或删除tag
    :param filepath: '~/.bash_profile'  # profile文件路径
    :param pattern: r'# app\.profile#start(.*?)# app\.profile#end'  # 正则表达式模式
    :param repl: 'new_content'  # 替换为的新内容
    :param is_new: 是否新增一个tag，True 新增tag，False 不会新增tag，删除时使用
    :return:
    """
    if len(filepath) == 0 or len(pattern) == 0 or not isinstance(repl, str):
        raise Exception('invalid filepath or pattern or repl')

    # 在 Unix 和 Windows 上，将参数中开头部分的 ~ 或 ~user 替换为当前 用户 的家目录并返回。
    profile_path = os.path.expanduser(filepath)
    if not os.path.exists(profile_path):
        return

    with open(profile_path, 'r') as file:
        content = file.read()  # 读取文件内容

    matches = re.findall(pattern, content, flags=re.DOTALL)
    if len(matches) > 0:
        content = re.sub(pattern, repl, content, flags=re.DOTALL)  # 修改匹配的内容：更新或删除
    else:
        if is_new:
            content += f'\n{repl}\n'
        else:
            return

    # 备份profile文件，用于出错时恢复
    backup_path = f'{profile_path}.appbak'
    if not os.path.exists(profile_path):
        shutil.copy2(profile_path, backup_path)

    with open(profile_path, 'w') as file:
        file.write(content)  # 写入文件内容

    os.remove(backup_path)  # 删除profile文件备份


if __name__ == '__main__':
    app_profile_uninstall()
    # install_appget_profile(PROFILE_DARWIN[0])
