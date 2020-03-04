%.png: %.tex
	xelatex -aux-directory=/tmp/ -shell-escape $<
	-rm $*.pdf $*.log $*.aux

%.tex: %.py
	python3 $< > $@
