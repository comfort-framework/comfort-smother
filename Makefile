default: help

.PHONY: help
help:
	@echo ""
	@echo "Targets:"
	@echo "    install      Install smother on your machine"
	@echo "    setup        Setup local development environment"
	@echo "                 (remember to \`. venv/bin/activate\`)"
	@echo "    test         Run full test suite"

WITH_ENV:=. venv/bin/activate;

venv: venv/bin/activate
venv/bin/activate: requirements_test.txt
	test -d venv || virtualenv venv
	$(WITH_ENV) pip install -Ur requirements_test.txt

.PHONY: clean
clean:
	python setup.py clean
	find comfortsmother -type d -name "__pycache__" -exec rm -fr "{}" +
	find tests -type d -name "__pycache__" -exec rm -fr "{}" +
	find comfortsmother -type d -name ".cache" -exec rm -fr "{}" +
	find tests -type d -name ".cache" -exec rm -fr "{}" +
	find comfortsmother -type f -name '*.pyc' -delete
	find tests -type f -name '*.pyc' -delete
	find comfortsmother -type f -name '*$py.class' -delete
	find tests -type f -name '*$py.class' -delete
	rm -f nosetests.xml
	rm -f memory_usage.txt
	rm -rf .cache
	rm -rf venv
	rm -f .comfortsmother
	rm -f .comfortsmother_log

.PHONY: setup
setup: clean venv
	$(WITH_ENV) python setup.py develop

.PHONY: install
install:
	python setup.py install

.PHONY: test
test: setup
	$(WITH_ENV) py.test --comfortsmother=comfortsmother -vv tests
