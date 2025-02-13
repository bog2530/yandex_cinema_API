from elasticsearch import AsyncElasticsearch
from redis import Redis


class FilmService:
    def __init__(self, redis: Redis, elastic: AsyncElasticsearch):
        self.redis = redis
        self.elastic = elastic

    ...
