# Don't rely on discipline

Code samples for my "Don't rely on discipline" talk.


Start with these:

```bash
$ pytest --cov-report html --cov=step1 step1.py
```

```python
>>> from step1 import han
```

```bash
$ mypy step2.py
```

Then follow the steps in https://github.com/zupo/discipline/blob/master/.circleci/config.yml
