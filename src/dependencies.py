from functools import lru_cache

from fastapi import Depends
from starlette.requests import Request
from elasticsearch import AsyncElasticsearch
from redis import Redis

from services.film_service import FilmService


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
