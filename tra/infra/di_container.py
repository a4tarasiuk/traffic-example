from typing import Generator

from bson import RawBSONDocument
from dependency_injector import containers, providers
from pymongo import MongoClient
from pymongo.database import Database

from tra.apps.forecast_rules.persistence.forecast_rule_memo_repo import ForecastRuleInMemoryRepository
from tra.apps.forecasting.model_factory import ForecastModelFactory
from tra.apps.forecasting.services import AbstractForecastingService, ForecastingService
from tra.apps.forecasting.services.capping import ForecastCappingService


def init_mongo_client() -> Generator[MongoClient[RawBSONDocument], None, None]:
    client: MongoClient[RawBSONDocument]
    with MongoClient() as client:  # TODO: Config
        yield client


def get_mongo_db(client: MongoClient[RawBSONDocument]) -> Database[RawBSONDocument]:
    return client["traffic"]  # TODO: Config


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["tra.apps.forecast_rules.rest.endpoints"],
    )

    mongo_client = providers.Resource(init_mongo_client)

    mongo_db = providers.Callable(get_mongo_db, client=mongo_client)

    forecast_rule_repository = providers.Singleton(ForecastRuleInMemoryRepository)

    forecasting_service = providers.Dependency(
        instance_of=AbstractForecastingService,  # type: ignore[type-abstract]
        default=providers.Factory(
            ForecastingService,
            forecast_model_factory=providers.Factory(ForecastModelFactory),
            capping_service=providers.Factory(ForecastCappingService),
        ),
    )
