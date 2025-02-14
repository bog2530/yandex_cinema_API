from uuid import UUID

from pydantic import BaseModel, Field


class Genres(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    name: str
