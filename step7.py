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
    def json(self: Person):
        return {
            "name": self.name,
            "mother": self.mother.name,
            "father": self.father.name,
        }

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


def test_json():
    assert luke.json == {
        "father": "Anakin Skywalker",
        "mother": "Padme Amidala",
        "name": "Luke Skywalker",
    }


def test_grandparents():
    assert luke.grandparents == [jobal, ruwee, shmi, force]
    assert han.grandparents == []
    assert kylo.grandparents == [padme, anakin]


""" Scenario:
$ pipenv run mypy step7.py
"""