from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.apps.forecasting.model_factory_abc import AbstractForecastModelFactory
from tra.apps.forecasting.models.abstract import AbstractForecastModel
from tra.apps.forecasting.models.f1 import F1ForecastModel
from tra.apps.forecasting.models.f2 import F2ForecastModel


class ForecastModelFactory(AbstractForecastModelFactory):
    def create(self, forecast_rule: ForecastRule) -> AbstractForecastModel:
        """Creates forecast model based on ForecastRule parameters."""

        match forecast_rule.forecast_model:
            case ForecastModelEnum.F1:
                return F1ForecastModel()

            case ForecastModelEnum.F2:
                return F2ForecastModel()

            case _:
                raise ValueError("Model is not supported")
