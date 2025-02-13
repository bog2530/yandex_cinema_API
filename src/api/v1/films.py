from typing import Annotated
from uuid import UUID

from fastapi import Depends, APIRouter, Query

from schemas.film import FilmShort, Film
from services.film_service import FilmService
from dependencies import get_film_service

roter = APIRouter(prefix="/films", tags=["films"])


@roter.get("")
async def get_films_all(
    sort: str | None = None,
    genre: str | None = None,
    page_size: int | None = 50,
    page_number: int | None = 0,
    film: FilmService = Depends(get_film_service),
) -> list[FilmShort]: ...


@roter.get("/{item_id}/")
async def get_film_by_id(
    item_id: UUID,
    film: FilmService = Depends(get_film_service),
) -> Film: ...


@roter.get("/search/")
async def get_films_search(
    query: Annotated[str, Query(max_length=128)],
    page_size: int | None = 50,
    page_number: int | None = 0,
    film: FilmService = Depends(get_film_service),
) -> list[FilmShort]: ...
