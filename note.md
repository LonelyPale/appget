
```shell
python3.9 -m venv venv
source venv/bin/activate
deactivate

pip list
pip install --upgrade pip
pip uninstall setuptools
pip uninstall --yes setuptools

pip install --upgrade setuptools wheel twine

python -m site
python -m pip install --upgrade build
python -m build
#Source distributions 源发行版
python -m build --sdist
#Pure Python Wheels
python -m build --wheel

python -m pip install --upgrade twine
python -m twine check dist/*
python -m twine upload --verbose --repository pypi dist/*
python -m twine upload --config-file .pypirc-my dist/*
python -m twine upload dist/*

pip install appget
pip install --upgrade appget
pip uninstall --yes appget

sudo python3 -m pip list
sudo python3 -m pip install appget --target=/usr/local/app/appget/lib
sudo python3 -m pip install appget --no-cache-dir --target=/usr/local/app/appget/lib

sudo sh -c "export PIP_NO_WARN_SCRIPT_LOCATION=1 && export PIP_DISABLE_PIP_VERSION_CHECK=1 && python3 -m pip install appget --no-cache-dir --target=/usr/local/app/appget/lib"

#测试
python -m pip install --upgrade pytest
python -m pytest --version

#命令行解析
pip install click
pip install fire
pip uninstall fire
#命令行着色
pip install colorama
#日志着色
pip install colorlog

# 测试本地执行
PYTHONPATH=./src python -m appget




```
WARNING: The directory '/Users/wyb/Library/Caches/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting appget
  Downloading appget-0.1.3-py3-none-any.whl.metadata (1.9 kB)
Downloading appget-0.1.3-py3-none-any.whl (5.8 kB)
Installing collected packages: appget
Successfully installed appget-0.1.3
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

export PIP_NO_WARN_SCRIPT_LOCATION=1
export PIP_DISABLE_PIP_VERSION_CHECK=1

