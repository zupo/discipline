# Based on https://github.com/teamniteo/Makefile

.PHONY: all
all: lint tests

.PHONY: lint
lint:
# 1. get all unstaged modified files
# 2. get all staged modified files
# 3. get all untracked files
# 4. run pre-commit checks on them
ifeq ($(all),true)
	@pre-commit run --hook-stage push --all-files
else
	@{ git diff --name-only ./; git diff --name-only --staged ./;git ls-files --other --exclude-standard; } \
			| sort | uniq \
			| xargs pre-commit run --hook-stage push --files
endif

.PHONY: tests
tests: .installed
	@pytest step*.py
