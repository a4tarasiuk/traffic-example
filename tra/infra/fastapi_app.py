from fastapi import FastAPI

from tra.apps.forecast_rules.infra.rest import forecast_rules_router
from tra.infra.di_container import DIContainer


def create_app() -> FastAPI:
    container = DIContainer()

    app = FastAPI()

    app.container = container

    app.include_router(forecast_rules_router)

    return app


app = create_app()
