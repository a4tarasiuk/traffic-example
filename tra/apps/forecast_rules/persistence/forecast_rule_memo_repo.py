from typing import Optional

from ulid import ULID

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecast_rules.domain.repositories import AbstractForecastRuleRepository


class ForecastRuleInMemoryRepository(AbstractForecastRuleRepository):
    def __init__(self) -> None:
        self._rules = []

    def create(self, rule: ForecastRule) -> ForecastRule:
        self._rules.append(rule)

        return rule

    def get_many(self) -> tuple[ForecastRule, ...]:
        return tuple(self._rules)

    def get_by_id(self, forecast_rule_id: ULID) -> Optional[ForecastRule]:
        return next((r for r in self._rules if r.id == forecast_rule_id), None)
