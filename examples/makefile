FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3         \
    Exceptions        \
    Types             \
    Operators         \
    Variables         \
    Cache             \
    Iteration         \
    Yield             \
    Lambda            \
    Comprehensions    \
    Iterables         \
    CommandLine       \
    FileInputOutput   \
    FormattedOutput   \
    FunctionKeywords  \
    FunctionDefaults  \
    FunctionUnpacking \
    FunctionTuple     \
    FunctionDict      \
    Sequences         \
    Lists             \
    Strings           \
    RegExps           \
    Sets              \
    Dicts

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
