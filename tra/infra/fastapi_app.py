from contextlib import asynccontextmanager

from fastapi import FastAPI

from tra.apps.forecast_rules.rest import forecast_rules_router
from tra.infra.di_container import DIContainer


@asynccontextmanager
async def lifespan(_app: FastAPI):  # type: ignore[no-untyped-def]

    yield

    _app.container.shutdown_resources()  # type: ignore[attr-defined]


def create_app() -> FastAPI:
    container = DIContainer()

    app = FastAPI(lifespan=lifespan)

    app.container = container  # type: ignore[attr-defined]

    app.include_router(forecast_rules_router)

    return app


app = create_app()
