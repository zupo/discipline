from __future__ import annotations

import json
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
    def json(self) -> t.Dict[str, t.Optional[str]]:
        return {
            "name": self.name,
            "mother": self.mother.name if self.mother else None,
            "father": self.father.name if self.father else None,
            "maternal_grandmother": self.mother.mother.name
            if self.mother and self.mother.mother
            else None,
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


def test_json():
    assert (
        json.dumps(han.json)
        == '{"name": "Han Solo", "mother": null, "father": null, "maternal_grandmother": null}'
    )
    assert (
        json.dumps(luke.json)
        == '{"name": "Luke Skywalker", "mother": "Padme Amidala", "father": "Anakin Skywalker", "maternal_grandmother": "Jobal Naberrie"}'
    )
    assert (
        json.dumps(anakin.json)
        == '{"name": "Anakin Skywalker", "mother": "Shmi Skywalker Lars", "father": "The Force", "maternal_grandmother": null}'
    )


def test_grandparents():
    assert luke.grandparents == [jobal, ruwee, shmi, force]
    assert han.grandparents == []
    assert kylo.grandparents == [padme, anakin]
