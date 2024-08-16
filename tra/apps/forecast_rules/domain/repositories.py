from abc import ABC, abstractmethod

from tra.apps.forecast_rules.domain.entities import ForecastRule


class AbstractForecastRuleRepository(ABC):
    @abstractmethod
    def create(self, rule: ForecastRule) -> ForecastRule:
        """Creates new rule."""

    @abstractmethod
    def get_many(self) -> tuple[ForecastRule, ...]:
        """Returns collection of Forecast Rule objects."""
