# Don't rely on discipline

Code samples for my "Don't rely on discipline" talk.

```bash
$ pytest --cov-report html --cov=step1 step1.py
```

```python
>>> from step1 import han
```

```bash
$ mypy step2.py
```




TODO:
* screenshot how many depsov pyupgrade pulls in
* screenshot of the same but for pre-commit
* spelling check
* fail if cicleci and shell.nix nixpkgs hashes don't match
* all these steps have tests of output, so I can work on them
