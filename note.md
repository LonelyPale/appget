
```shell
python3.9 -m venv venv
source venv/bin/activate
deactivate

pip list
pip install --upgrade pip
pip uninstall setuptools

pip install --upgrade setuptools wheel twine

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
pip uninstall --yes appget

```
