FILES :=            \
    IsPrime1T       \
    IsPrime2T       \
    FactorialT      \
    ReduceT         \
    DigitsIteratorT \
    DigitsT         \
    MapT            \
    RMSET           \
    ComplexT        \
    TheatreSquareT

%.pyx: %.py
	coverage run --branch ./$<
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
