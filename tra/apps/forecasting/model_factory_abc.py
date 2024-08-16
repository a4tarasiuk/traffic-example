from abc import ABC

from tra.apps.forecasting.models.abstract import AbstractForecastModel
from tra.apps.forecast_rules.domain.entities import ForecastRule


class AbstractForecastModelFactory(ABC):
    def create(self, forecast_rule: ForecastRule) -> AbstractForecastModel:
        """Creates forecast model based on ForecastRule parameters."""
