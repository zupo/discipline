### Model ###
from __future__ import annotations

import typing as t


class Person:
    mother: t.Optional[Person]
    father: t.Optional[Person]

    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def __repr__(self):
        return self.name

    @property
    def grandparents(self: Person) -> t.List[Person]:
        grandparents = []
        if self.mother:
            grandparents.append(self.mother.mother)
            grandparents.append(self.mother.father)
        if self.father:
            grandparents.append(self.father.mother)
            grandparents.append(self.father.father)
        return [person for person in grandparents if person is not None]


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
    assert han.grandparents == []
    assert kylo.grandparents == [padme, anakin]


""" Scenario:
$ pipenv run pytest --cov=step5 --cov-branch --cov-fail-under=100 --cov-report html step5.py
$ open htmlcov/index.html
$ pipenv run mypy step5.py
$ pipenv run python
>>> from step5 import kylo, han
>>> han.grandparents
>>> kylo.grandparents
"""
