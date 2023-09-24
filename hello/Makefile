PY = python3
PYFLAGS = -m
PYTEST = pytest
PYTESTFLAGS = -v
FLAKE = flake8
FLAKEFLAGS = --count --show-source --statistics
PYLINT = pylint
PYLINTFLAGS = --max-line-length=100

.PHONY: all
all: check_style lint black check_security unittest localtest run submit


.PHONY: unittest
unittest:
	$(PY) $(PYFLAGS) $(PYTEST) $(PYTESTFLAGS) test_hello.py
	$(PY) $(PYFLAGS) $(PYTEST) $(PYTESTFLAGS) test_unittest.py

.PHONY: test
localtest:
	@echo "No sample test cases for this problem."

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache

.PHONY: run
run:
	$(PY) $(PYFLAGS) hello

.PHONY: check_style
check_style:
	$(PY) $(PYFLAGS) $(FLAKE) $(FLAKEFLAGS) hello.py

.PHONY: lint
lint:
	$(PY) $(PYFLAGS) $(PYLINT) $(PYLINTFLAGS) hello.py
	$(PY) $(PYFLAGS) $(PYLINT) $(PYLINTFLAGS) test_hello.py

.PHONY: type_check
type_check:
	mypy --disallow-untyped-defs --strict hello.py
	mypy --disallow-untyped-defs --strict test_hello.py
	mypy --disallow-untyped-defs --strict test_unittest.py

.PHONY: check_security
check_security:
	bandit -r hello.py > hello_bandit.txt
	#bandit -r test_hello.py
	bandit -r test_unittest.py > test_unittest_bandit.txt

.PHONY: black
black:
	black hello.py
	black test_hello.py
	black test_unittest.py

.PHONY: submit
submit:
	kattis -f -p hello hello.py
