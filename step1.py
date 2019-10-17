### Model ###


class Person:
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def __repr__(self):
        return self.name

    @property
    def grandparents(self):
        grandparents = []
        grandparents.append(self.mother.mother)
        grandparents.append(self.mother.father)
        grandparents.append(self.father.mother)
        grandparents.append(self.father.father)
        return grandparents


### Data ###

jobal = Person("Jobal Naberrie")
ruwee = Person("Ruwee Naberrie")
padme = Person("Padme Amidala", mother=jobal, father=ruwee)

shmi = Person("Shmi Skywalker Lars")
force = Person("The Force")
anakin = Person("Anakin Skywalker", mother=shmi, father=force)

luke = Person("Luke Skywalker", mother=padme, father=anakin)
leia = Person("Leia Organa", mother=padme, father=anakin)

han = Person("Han Solo")
kylo = Person("Kylo Ren", mother=leia, father=han)


### Tests ###


def test_person():
    foo = Person("foo")
    assert f"{foo}" == "foo"
    assert foo.name == "foo"


def test_grandparents():
    assert luke.grandparents == [jobal, ruwee, shmi, force]


""" Scenario:
$ pipenv run pytest --cov=step1 --cov-report html --cov-branch step1.py
$ open htmlcov/index.html
$ pipenv run python
>>> from step1 import kylo, han
>>> kylo.grandparents
[Padme Amidala, Anakin Skywalker, None, None]  # <- not ideal
>>> han.grandparents
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "~/step1.py", line 16, in grandparents
    grandparents.append(self.mother.mother)
AttributeError: 'NoneType' object has no attribute 'mother'
"""
