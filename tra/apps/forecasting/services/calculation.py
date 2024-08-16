from decimal import Decimal

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecasting.services.capping_abc import AbstractForecastCappingService
from tra.apps.forecasting.model_factory_abc import AbstractForecastModelFactory
from tra.apps.forecasting.services.calculation_abc import AbstractForecastingService


class ForecastingService(AbstractForecastingService):
    """
    Performs forecast rule calculation based on its parameters which include application of appropriate forecast model.
    Applies capping rule to forecasting result.
    """

    def __init__(
        self,
        forecast_model_factory: AbstractForecastModelFactory,
        capping_service: AbstractForecastCappingService,
    ) -> None:
        self._forecast_model_factory = forecast_model_factory

        self._capping_service = capping_service

    def calculate(self, forecast_rule: ForecastRule) -> Decimal:
        model = self._forecast_model_factory.create(forecast_rule)

        result = model.calculate(forecast_rule)

        result = self._capping_service.apply_to(result)

        return result
