from dependency_injector import containers, providers

from tra.apps.forecast_rules.infra.forecast_rule_memo_repo import ForecastRuleInMemoryRepository
from tra.apps.forecasting.model_factory import ForecastModelFactory
from tra.apps.forecasting.services import AbstractForecastingService, ForecastingService
from tra.apps.forecasting.services.capping import ForecastCappingService


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["tra.apps.forecast_rules.infra.rest.endpoints"],
    )

    forecast_rule_repository = providers.Singleton(ForecastRuleInMemoryRepository)

    forecasting_service = providers.Dependency(
        instance_of=AbstractForecastingService,
        default=providers.Factory(
            ForecastingService,
            forecast_model_factory=providers.Factory(ForecastModelFactory),
            capping_service=providers.Factory(ForecastCappingService),
        ),
    )
