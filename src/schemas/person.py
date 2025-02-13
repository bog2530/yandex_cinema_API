from uuid import UUID

from pydantic import BaseModel, Field


class Person(BaseModel):
    id: UUID = Field(alias="uuid")
    full_name: str


class Role(BaseModel):
    id: UUID = Field(alias="uuid")
    name: list[str] = Field(default=[])


class PersonFilm(Person):
    films: list[Role] = Field(default=[])
