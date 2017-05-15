TESTPYPI = https://testpypi.python.org/pypi

install:
	pip install .

develop:
	pip install -e .[dev]

uninstall:
	pip uninstall casoff_vcf

upload:
	python setup.py register
	python setup.py sdist upload

test-upload:
	python setup.py register -r $(TESTPYPI)
	python setup.py sdist upload -r $(TESTPYPI)

test-install:
	pip install -i $(TESTPYPI) casoff-vcf

test: develop
	py.test -v --doctest-modules casoff_vcf.py test_casoff_vcf.py

.PHONY: install develop uninstall upload test-upload test-install test
