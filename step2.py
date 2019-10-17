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
    def grandparents(self: Person):
        grandparents = []
        grandparents.append(self.mother.mother)
        grandparents.append(self.mother.father)
        grandparents.append(self.father.mother)
        grandparents.append(self.father.father)
        return grandparents


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


def test_person():
    foo = Person("foo")
    assert f"{foo}" == "foo"
    assert foo.name == "foo"


def test_grandparents():
    assert luke.grandparents == [jobal, ruwee, shmi, force]
