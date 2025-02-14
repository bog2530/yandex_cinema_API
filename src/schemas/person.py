from uuid import UUID

from pydantic import BaseModel, Field


class Person(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    full_name: str = Field(alias="name", serialization_alias="full_name")


class Role(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    name: list[str] = Field(default=[])


class PersonFilm(Person):
    films: list[Role] = Field(default=[])
