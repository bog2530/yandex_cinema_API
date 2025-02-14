from uuid import UUID

from pydantic import BaseModel, Field

from schemas.genre import Genres
from schemas.person import Person


class FilmShort(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    title: str
    imdb_rating: float


class Film(FilmShort):
    description: str
    genres: list[str] = Field(default=[])  # toDo name - genre, class - Genres
    actors: list[Person] = Field(default=[])
    writers: list[Person] = Field(default=[])
    directors: list[Person] = Field(default=[])
