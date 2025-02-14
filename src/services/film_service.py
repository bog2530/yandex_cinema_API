from typing import Optional
from uuid import UUID

from elasticsearch import AsyncElasticsearch, NotFoundError
from redis import Redis

from schemas.film import Film, FilmShort


class FilmService:
    def __init__(self, redis: Redis, elastic: AsyncElasticsearch, index_name: str):
        self.redis = redis
        self.elastic = elastic
        self.index = index_name

    async def _search_es(self, **kwargs):
        return await self.elastic.search(kwargs)

    async def all(
        self,
        query: str | None = None,
        sort: tuple[str, str] | None = None,
        genre: str | None = None,
        page_size: int = 50,
        page_number: int = 0,
    ) -> list[FilmShort]:
        offset = page_size * page_number

        body = {
            "query": {"match_all": {}},
            "_source": ["id", "title", "imdb_rating"],
        }
        if query:
            body["query"] = {"match": {"title": query}}
        if genre:
            body["query"] = {"match": {"genre": genre}}
        if sort:
            body["sort"] = [{sort[0]: {"order": sort[1]}}]

        response = await self.elastic.search(
            index=self.index,
            size=page_size,
            from_=offset,
            body=body,
        )
        return [
            FilmShort(**item["_source"])
            for item in response.get("hits", {}).get("hits", [])
        ]

    async def by_id(self, item_id: UUID) -> Optional[Film]:
        try:
            response = await self.elastic.get(
                index=self.index,
                id=item_id,
            )
        except NotFoundError:
            return None
        return Film(**response["_source"])

    # async def _get_cache(self, film_id: str) -> Optional[Film]:
    #     data = await self.redis.get(film_id)
    #     if not data:
    #         return None
    #
    #     film = Film.model_validate_json(data)
    #     return film
    #
    # async def _put_film_to_cache(self, film: Film):
    #     await self.redis.set(
    #         str(film.id), film.model_dump_json(), FILM_CACHE_EXPIRE_IN_SECONDS
    #     )
