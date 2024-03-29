import os
import re


def a():
    profile_path = os.path.expanduser('~/.bash_profile')
    profile_path = os.path.expanduser('~/bash_profile.bak')
    # profile_path = os.path.expanduser('~/PycharmProjects/appget/src/appget/temp.py')
    with open(profile_path, 'r') as file:
        content = file.read()
        b = []
        for x in content:
            b.append(x)
        b.reverse()
        c = content[-2:]
    print(content)

    my_string = "h\ne\nl\nl\no\n\n\n"
    new_string = my_string.rstrip('\n')
    print(new_string+'\n')


def b():
    pattern = r'(\n*)# app\.profile#start(.*?)# app\.profile#end(\n*)'
    profile_path = os.path.expanduser('~/.bash_profile')
    with open(profile_path, 'r') as file:
        content = file.read()
        l = list(content)
    matches = re.findall(pattern, content, flags=re.DOTALL)
    content_new = re.sub(pattern, r'\1repl\3', content, flags=re.DOTALL)  # 修改匹配的内容：更新或删除
    print(matches)




if __name__ == '__main__':
    b()
