FILES :=              \
    Hello             \
    Exceptions        \
    Types             \
    Operators         \
    Variables         \
    Cache

%.pyx: %.py
	coverage run --branch ./$<
	coverage report -m

CommandLine.pyx: CommandLine.py
	coverage run --branch ./CommandLine.py Nothing to be done.
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
