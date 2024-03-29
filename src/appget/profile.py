import os
import re
import shutil

from appget.constant import APP_PROFILE
from appget.system import is_linux, is_darwin

# 在linux中，一般情况下.profile中会导入.bashrc，
# .bashrc是每次打开一个新的终端窗口（bash shell）时都会执行的文件。
# .profile是登录(login)时执行的文件，即当用户登录时会执行一次。
PROFILE_LINUX = ['~/.bashrc']

# .bash_profile文件是macOS系统中Bash shell的默认登录脚本。
PROFILE_DARWIN = ['~/.bash_profile']

APPNAME_KEY = '{appname}'
CONTENT_KEY = '{content}'
CONTENT = '''

# app.{appname}#start
{content}
# app.{appname}#end

'''
PATTERN = r'(\n*)# app\.{appname}#start(.*?)# app\.{appname}#end(\n*)'  # 正则表达式模式

APPGET_PROFILE_APPNAME_VAL = 'profile'
APPGET_PROFILE_CONTENT_VAL = f'[[ -s "{APP_PROFILE}" ]] && source "{APP_PROFILE}"'


def get_profile_paths():
    if is_linux():
        return PROFILE_LINUX
    elif is_darwin():
        return PROFILE_DARWIN
    else:
        return []


def appget_profile_install():
    pattern = PATTERN.replace(APPNAME_KEY, APPGET_PROFILE_APPNAME_VAL)
    repl = (CONTENT.replace(APPNAME_KEY, APPGET_PROFILE_APPNAME_VAL)
            .replace(CONTENT_KEY, APPGET_PROFILE_CONTENT_VAL))
    for filepath in get_profile_paths():
        update(filepath, pattern, repl)


def appget_profile_uninstall():
    pattern = PATTERN.replace(APPNAME_KEY, APPGET_PROFILE_APPNAME_VAL)
    repl = '\n\n'  # 删除 app tag 时，保留一个空行 \n\n
    for filepath in get_profile_paths():
        update(filepath, pattern, repl, is_new=False)


def app_profile_install(appname, content):
    if len(appname) == 0 or len(content) == 0:
        raise Exception(f'invalid app profile appname={appname} or content={content}')

    pattern = PATTERN.replace(APPNAME_KEY, appname)
    repl = (CONTENT.replace(APPNAME_KEY, appname)
            .replace(CONTENT_KEY, content))
    update(APP_PROFILE, pattern, repl)


def app_profile_uninstall(appname):
    if len(appname) == 0:
        raise Exception(f'invalid app profile appname={appname}')

    pattern = PATTERN.replace(APPNAME_KEY, appname)
    repl = '\n\n'  # 删除 app tag 时，保留一个空行 \n\n
    update(APP_PROFILE, pattern, repl, is_new=False)


def update(filepath, pattern, repl, is_new=True):
    """
    修改profile文件内容，更新或删除tag
    :param filepath: '~/.bash_profile'  # profile文件路径
    :param pattern: r'(\n*)# app\.profile#start(.*?)# app\.profile#end(\n*)'  # 正则表达式模式
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
            content = content.rstrip('\n')  # 新增 app tag 前，删除字符串末尾的全部\n
            content += repl
        else:
            return

    # 备份profile文件，用于出错时恢复
    backup_path = f'{profile_path}.appbak'
    if not os.path.exists(backup_path):
        shutil.copy2(profile_path, backup_path)

    with open(profile_path, 'w') as file:
        file.write(content)  # 写入文件内容

    os.remove(backup_path)  # 删除profile文件备份
