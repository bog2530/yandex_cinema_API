from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from elasticsearch import AsyncElasticsearch
from redis.asyncio import Redis

from core.settings import settings, Settings
from api import list_of_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    app.es = AsyncElasticsearch(
        hosts=[
            f"{settings.ELASTIC_SCHEMA}{settings.ELASTIC_HOST}:{settings.ELASTIC_PORT}"
        ]
    )
    yield
    await app.redis.close()
    await app.es.close()


def get_app() -> FastAPI:
    def bind_routes(application: FastAPI, setting: Settings) -> None:
        for route in list_of_routes:
            application.include_router(route, prefix=setting.PATH_PREFIX)

    application = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/docs",
        openapi_url="/openapi",
        version="0.0.1",
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
