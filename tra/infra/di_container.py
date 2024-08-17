from dependency_injector import containers, providers

from tra.apps.forecast_rules.persistence.forecast_rule_mongo_repo import ForecastRuleMongoRepository
from tra.apps.forecasting.model_factory import ForecastModelFactory
from tra.apps.forecasting.services import AbstractForecastingService, ForecastingService
from tra.apps.forecasting.services.capping import ForecastCappingService
from tra.infra.persistence import get_mongo_db, init_mongo_client


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["tra.apps.forecast_rules.rest.endpoints"],
    )

    mongo_client = providers.Resource(init_mongo_client)

    mongo_db = providers.Callable(get_mongo_db, client=mongo_client)

    forecast_rule_repository = providers.Factory(
        ForecastRuleMongoRepository,
        mongo_db=mongo_db,
    )

    forecasting_service = providers.Dependency(
        instance_of=AbstractForecastingService,  # type: ignore[type-abstract]
        default=providers.Factory(
            ForecastingService,
            forecast_model_factory=providers.Factory(ForecastModelFactory),
            capping_service=providers.Factory(ForecastCappingService),
        ),
    )
