from dependency_injector import containers, providers

from tra.apps.forecast_rules.infra.forecast_rule_memo_repo import ForecastRuleInMemoryRepository


class DIContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["tra.apps.forecast_rules.infra.rest.endpoints"],
    )

    forecast_rule_repository = providers.Singleton(ForecastRuleInMemoryRepository)
