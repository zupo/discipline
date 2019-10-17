### Model ###
from __future__ import annotations
from dataclasses import dataclass
from dataclasses import field

import json
import typing as t


@dataclass
class Person:
    name: str
    mother: t.Optional[Person] = None
    father: t.Optional[Person] = None

    @property
    def json(self: Person) -> t.Dict[str, t.Optional[str]]:
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


def test_json() -> None:
    assert (
        json.dumps(han.json)
        == '{"name": "Han Solo", "mother": null, "father": null, "maternal_grandmother": null}'
    )
    assert (
        json.dumps(luke.json)
        == '{"name": "Luke Skywalker", "mother": "Padme Amidala", "father": "Anakin Skywalker", "maternal_grandmother": "Jobal Naberrie"}'
    )


def test_grandparents() -> None:
    assert luke.grandparents == [jobal, ruwee, shmi, force]
    assert han.grandparents == []
    assert kylo.grandparents == [padme, anakin]
