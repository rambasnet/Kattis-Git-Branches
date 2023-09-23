PY = python3
PYFLAGS = -m
PYTEST = pytest
PYTESTFLAGS = -v

.PHONY: all
all: test

.PHONY: test
test:
	$(PY) $(PYFLAGS) $(PYTEST) $(PYTESTFLAGS)

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache
	