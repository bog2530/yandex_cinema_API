from uuid import UUID

from fastapi import Depends, APIRouter

from schemas.genres import Genres
from services.genre_service import GenreService
from dependencies import get_genre_service

roter = APIRouter(prefix="/genres", tags=["genres"])


@roter.get("/")
async def get_genres_all(
    film: GenreService = Depends(get_genre_service),
) -> list[Genres]: ...


@roter.get("/{genre_id}/")
async def get_genre_by_id(
    genre_id: UUID,
    film: GenreService = Depends(get_genre_service),
) -> Genres: ...
