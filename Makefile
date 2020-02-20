%.png: %.tex
	xelatex -aux-directory=/tmp/ -shell-escape $<

%.tex: %.py
	python3 $< > $@
