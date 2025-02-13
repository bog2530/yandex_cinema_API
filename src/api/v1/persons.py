from typing import Annotated
from uuid import UUID

from fastapi import Depends, APIRouter, Query

from schemas.person import Person, PersonFilm
from services.film_service import FilmService
from dependencies import get_film_service

roter = APIRouter(prefix="/persons", tags=["persons"])


@roter.get("/{item_id}/film/")
async def get_films_by_person(
    item_id: UUID,
    film: FilmService = Depends(get_film_service),
) -> list[PersonFilm]: ...


@roter.get("/{item_id}/")
async def get_person_by_id(
    item_id: UUID,
    film: FilmService = Depends(get_film_service),
) -> PersonFilm: ...


@roter.get("/search/")
async def get_persons_search(
    query: Annotated[str, Query(max_length=128)],
    page_size: int | None = 50,
    page_number: int | None = 0,
    film: FilmService = Depends(get_film_service),
) -> list[PersonFilm]: ...
