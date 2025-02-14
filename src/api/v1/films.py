from typing import Annotated, Optional
from uuid import UUID
from enum import Enum

from fastapi import Depends, APIRouter, Query, HTTPException

from schemas.film import FilmShort, Film
from services.film_service import FilmService
from dependencies import get_film_service

roter = APIRouter(prefix="/films", tags=["films"])


# toDo Вынести enum
class SortFilm(str, Enum):
    imdb_rating_asc = "+imdb_rating"
    imdb_rating_desc = "-imdb_rating"

    @property
    def sort_tuple(self):
        match self:
            case SortFilm.imdb_rating_desc:
                return "imdb_rating", "desc"
            case SortFilm.imdb_rating_asc:
                return "imdb_rating", "asc"
            case _:
                return None


# toDO Проверить подбор по жанрам
@roter.get("")
async def get_films_all(
    sort: SortFilm | None = None,
    genre: str | None = None,
    page_size: Annotated[int, Query(le=200)] = 50,
    page_number: int | None = 0,
    film: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    if sort:
        sort = sort.sort_tuple
    return await film.all(
        sort=sort, genre=genre, page_size=page_size, page_number=page_number
    )


@roter.get("/search/")
async def get_films_search(
    query: Annotated[str, Query(max_length=256)],
    page_size: int | None = 50,
    page_number: int | None = 0,
    film: FilmService = Depends(get_film_service),
) -> list[FilmShort]:
    return await film.all(query=query, page_size=page_size, page_number=page_number)


# toDo Вынести схему и исключение
# toDo Добавить uuid к жанрам
@roter.get(
    "/{item_id}/",
    responses={
        404: {
            "description": "Film not found",
            "content": {"application/json": {"example": {"detail": "Film not found"}}},
        }
    },
)
async def get_film_by_id(
    item_id: UUID,
    film: FilmService = Depends(get_film_service),
) -> Film:
    result = await film.by_id(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Film not found")
    return result
