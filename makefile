.DEFAULT_GOAL := test

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    MYPY     := mypy
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

clean:
	cd examples; make clean
	@echo
	cd exercises; make clean

config:
	git config -l

docker-build:
	docker build -t gpdowning/python .

docker-pull:
	docker pull gpdowning/python

docker-push:
	docker push gpdowning/python

docker-run:
	docker run -it -v $(PWD):/usr/jpl -w /usr/jpl gpdowning/python

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/oopl-jpl.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .travis.yml
	git add Dockerfile
	git add examples
	git add exercises
	git add makefile
	git add notes
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete              \
    --include "Docker.txt"                   \
    --include "Hello.py"                     \
    --include "Assertions.py"                \
    --include "Exceptions.py"                \
    --include "Types.py"                     \
    --include "Operators.py"                 \
    --include "Variables.py"                 \
    --include "Copy.py"                      \
    --include "Cache.py"                     \
    --include "Iteration.py"                 \
    --include "Lambdas.py"                   \
    --include "Comprehensions.py"            \
    --include "Yield.py"                     \
    --include "Iterables.py"                 \
    --include "MyPy.py"                      \
    --include "FileInputOutput.py"           \
    --include "FormattedOutput.py"           \
    --include "GlobalVariables.py"           \
    --include "Classes.py"                   \
    --include "FunctionKeywords.py"          \
    --include "FunctionDefaults.py"          \
    --include "FunctionUnpacking.py"         \
    --include "FunctionTuple.py"             \
    --include "FunctionDict.py"              \
    --exclude "*"                            \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete              \
    --include "UnitTests1.py"                \
    --include "UnitTests1T.py"               \
    --include "UnitTests2.py"                \
    --include "UnitTests2T.py"               \
    --include "UnitTests3.py"                \
    --include "UnitTests3T.py"               \
    --include "Coverage1.py"                 \
    --include "Coverage1T.py"                \
    --include "Coverage2.py"                 \
    --include "Coverage2T.py"                \
    --include "Coverage3.py"                 \
    --include "Coverage3T.py"                \
    --include "IsPrime1.py"                  \
    --include "IsPrime1T.py"                 \
    --include "IsPrime2.py"                  \
    --include "IsPrime2T.py"                 \
    --include "Factorial.py"                 \
    --include "FactorialT.py"                \
    --include "Reduce.py"                    \
    --include "ReduceT.py"                   \
    --include "RMSE.py"                      \
    --include "RMSET.py"                     \
    --include "Map.py"                       \
    --include "MapT.py"                      \
    --include "RangeIterator.py"             \
    --include "RangeIteratorT.py"            \
    --include "Range.py"                     \
    --include "RangeT.py"                    \
    --include "Complex.py"                   \
    --include "ComplexT.py"                  \
    --include "Reduce2.py"                   \
    --include "Reduce2T.py"                  \
    --include "Map2.py"                      \
    --include "Map2T.py"                     \
    --include "Zip.py"                       \
    --include "ZipT.py"                      \
    --exclude "*"                            \
    ../../exercises/python/ exercises

test:
	make clean
	@echo
	cd examples; make test
	@echo
	cd exercises; make test

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(MYPY)
	$(MYPY) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	-which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list
