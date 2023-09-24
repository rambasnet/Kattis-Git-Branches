# provide path to where plantuml.jar is downloaded
PLANTUML = java -jar ../plantuml.jar
DOCS = docs
PY = python3
PYFLAGS = -m
PYTEST = pytest
PYTESTFLAGS = -v
FLAKE = flake8
FLAKEFLAGS = --count --show-source --statistics
PYLINT = pylint
PYLINTFLAGS = --max-line-length=100

# not required but recommended to add .PHONY target for every target
.PHONY: all
all: check_style check_types lint unittest localtest create_docs create_uml
	@echo "All done!"

unittest:
ifeq ($(shell which pytest), ) # if pytest not found
	@echo "pytest not found. Installing..."
	pip install pytest
endif
	$(PYTEST) $(PYTESTFLAGS) tests
	@echo "All unittesting worked!"

localtest:
	@python main.py | diff - data/1.ans
	@echo "Program worked on sample data!" 

check_types:
# use shell command which to check if mypy is installed and is in $PATH
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict main.py hello.py
	mypy --disallow-untyped-defs --strict tests
	@echo "Type checking done."

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc -o $(DOCS) main.py hello.py # creates html docs inside docs
	pdoc -o $(DOCS) main.py hello.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

create_uml: create_doc_folder
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ../plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ..//plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	$(PLANTUML) uml/HelloWorld.plantuml
	$(PLANTUML) uml/Main.plantuml
	$(PLANTUML) uml/solution.plantuml
	@echo "UML diagrams created and saved in uml folder"

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache

.PHONY: check_security
check_security:
	bandit -r hello.py > hello_bandit.txt

.PHONY: black
black:
	black hello.py
	black tests

.PHONY: check_style
check_style:
	$(PY) $(PYFLAGS) $(FLAKE) $(FLAKEFLAGS) hello.py main.py
	$(PY) $(PYFLAGS) $(FLAKE) $(FLAKEFLAGS) tests

.PHONY: submit
submit:
	kattis -f -p hello hello.py main.py


.PHONY: lint
lint:
	$(PY) $(PYFLAGS) $(PYLINT) $(PYLINTFLAGS) hello.py main.py
	$(PY) $(PYFLAGS) $(PYLINT) $(PYLINTFLAGS) tests