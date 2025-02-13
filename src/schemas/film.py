from uuid import UUID

from pydantic import BaseModel, Field

from schemas.genre import Genres
from schemas.person import Person


class FilmShort(BaseModel):
    id: UUID = Field(alias="uuid")
    title: str
    imdb_rating: float


class Film(BaseModel):
    id: UUID = Field(alias="uuid")
    title: str
    imdb_rating: float
    description: str
    genre: list[Genres] = Field(default=[])
    actors: list[Person] = Field(default=[])
    writers: list[Person] = Field(default=[])
    directors: list[Person] = Field(default=[])
