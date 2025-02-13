from functools import lru_cache

from fastapi import Depends
from starlette.requests import Request
from elasticsearch import AsyncElasticsearch
from redis import Redis

from services.film_service import FilmService
from services.genre_service import GenreService
from services.person_service import PersonService


async def get_elastic(request: Request) -> AsyncElasticsearch:
    return request.app.es


async def get_redis(request: Request) -> Redis:
    return request.app.redis


@lru_cache()
def get_film_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> FilmService:
    return FilmService(redis, elastic)


@lru_cache()
def get_genre_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> GenreService:
    return GenreService(redis, elastic)


@lru_cache()
def get_person_service(
    redis: Redis = Depends(get_redis),
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonService:
    return PersonService(redis, elastic)
