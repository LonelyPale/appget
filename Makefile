.PHONY: docs

init:
	#python -m pip install -r requirements-dev.txt
	python -m pip install --upgrade build twine

publish: clean
	python -m build
	python -m twine upload --config-file .pypirc-my dist/*

clean:
	rm -rf dist src/appget.egg-info

test:
	# This runs all of the tests on all supported Python versions.
	tox -p

ci:
	python -m pytest tests --junitxml=report.xml

test-readme:
	python setup.py check --restructuredtext --strict && ([ $$? -eq 0 ] && echo "README.rst and HISTORY.rst ok") || echo "Invalid markup in README.rst or HISTORY.rst!"

flake8:
	python -m flake8 src/requests

coverage:
	python -m pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=src/requests tests

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
