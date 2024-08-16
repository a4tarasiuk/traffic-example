from abc import ABC, abstractmethod
from decimal import Decimal

from tra.apps.forecast_rules.domain.entities import ForecastRule


class AbstractForecastModel(ABC):
    @abstractmethod
    def calculate(self, forecast_rule: ForecastRule) -> Decimal:
        """Calculates forecasted volume."""
