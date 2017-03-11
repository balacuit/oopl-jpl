FILES :=            \
    UnitTests3T     \
    Coverage1T      \
    Coverage2T      \
    Coverage3T      \
    IsPrime1T

%.pyx: %.py
	coverage run --branch ./$<
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
