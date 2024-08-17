from abc import ABC, abstractmethod

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecasting.models.abstract import AbstractForecastModel


class AbstractForecastModelFactory(ABC):
    @abstractmethod
    def create(self, forecast_rule: ForecastRule) -> AbstractForecastModel:
        """Creates forecast model based on ForecastRule parameters."""
