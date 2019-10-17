# Based on https://github.com/niteoweb/Makefile
.EXPORT_ALL_VARIABLES:
PIPENV_VENV_IN_PROJECT = 1
PIPENV_IGNORE_VIRTUALENVS = 1

.PHONY: all
all: .installed format tests

.PHONY: install
install:
	@rm -f .installed  # force re-install
	@make .installed

.installed: Pipfile Pipfile.lock
	@echo "Pipfile(.lock) is newer than .installed, (re)installing"
	@pipenv sync --dev
	@echo "This file is used by 'make' for keeping track of last install time. If Pipfile or Pipfile.lock are newer then this file (.installed) then all 'make *' commands that depend on '.installed' know they need to run pipenv install first." \
		> .installed

.PHONY: format
format: .installed
	@pipenv run black step*.py


.PHONY: tests
tests: .installed
	@pipenv run pytest step*.py

.PHONY: clean
clean:
	@if [ -d ".venv/" ]; then pipenv --rm; fi
	@rm -rf .coverage .mypy_cache/ htmlcov/ output.txt output.txt.head output.txt.tail
	@rm -f .installed
