from uuid import UUID

from pydantic import BaseModel, Field


class Genres(BaseModel):
    id: UUID = Field(alias="uuid")
    name: str
