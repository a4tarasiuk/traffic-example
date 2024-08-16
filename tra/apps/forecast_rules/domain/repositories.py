from abc import ABC, abstractmethod

from typing_extensions import Optional
from ulid import ULID

from tra.apps.forecast_rules.domain.entities import ForecastRule


class AbstractForecastRuleRepository(ABC):
    @abstractmethod
    def create(self, rule: ForecastRule) -> ForecastRule:
        """Creates new rule."""

    @abstractmethod
    def get_many(self) -> tuple[ForecastRule, ...]:
        """Returns collection of Forecast Rule objects."""

    @abstractmethod
    def get_by_id(self, forecast_rule_id: ULID) -> Optional[ForecastRule]:
        """Returns Forecast Rule instance by provided ID."""
