LOCALISED_SCRIPTS = ipython ipdb flake8 pylint nose
PROJECT = $(shell basename $(shell pwd))

all: check 

bootstrap: dev.nix requirements.txt setup.py
	nix-env -p nixprofile -i dev-env -f dev.nix
	./nixprofile/bin/virtualenv --distribute --clear .
	echo ../../../nixprofile/lib/python2.7/site-packages > lib/python2.7/site-packages/nixprofile.pth
	./bin/pip install -r requirements.txt --no-index -f ""
	for script in ${LOCALISED_SCRIPTS}; do ./bin/easy_install -H "" $$script; done


print-syspath:
	./bin/python -c 'import sys,pprint;pprint.pprint(sys.path)'


var:
	test -L var -a ! -e var && rm var || true
	ln -s $(shell mktemp --tmpdir -d ${PROJECT}-var-XXXXXXXXXX) var

var-clean:
	rm -fR var/*

check: var var-clean
	./bin/nosetests -v -w . --processes=4 ${ARGS}

check-debug: var var-clean
	DEBUG=1 ./bin/nosetests -v -w . --ipdb --ipdb-failures ${ARGS}

coverage: var var-clean bin/nosetests
	rm -f .coverage
	./bin/nosetests -v -w . --with-cov --cover-branches --cover-package=${PROJECT} ${ARGS}


pyoc-clean:
	find . -name '*.py[oc]' -print0 |xargs -0 rm

.PHONY: all bootstrap check check-debug coverage print-syspath pyoc-clean var var-clean
