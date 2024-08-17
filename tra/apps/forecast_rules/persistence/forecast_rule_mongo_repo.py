from decimal import Decimal
from typing import Any, Optional

from pymongo.database import Database
from ulid import ULID

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.apps.forecast_rules.domain.repositories import AbstractForecastRuleRepository
from tra.core.enums import DirectionEnum


class ForecastRuleMongoRepository(AbstractForecastRuleRepository):
    def __init__(self, mongo_db: Database[dict[str, Any]]) -> None:
        self._mongo_db = mongo_db

        self._collection = self._mongo_db["forecast_rules"]

    def create(self, rule: ForecastRule) -> ForecastRule:
        document = rule.model_dump(mode="json")

        self._collection.insert_one(document)

        _rule = self.get_by_id(rule.id)

        if _rule is None:
            raise ValueError("Forecast rule must exist")

        return _rule

    def get_many(self) -> tuple[ForecastRule, ...]:
        forecast_rules = map(from_mongo_document_to_forecast_rule, self._collection.find({}))

        return tuple(forecast_rules)

    def get_by_id(self, forecast_rule_id: ULID) -> Optional[ForecastRule]:
        doc = self._collection.find_one({"id": str(forecast_rule_id)})

        if doc:
            return from_mongo_document_to_forecast_rule(doc)

        return None


def from_mongo_document_to_forecast_rule(doc: dict[str, Any]) -> ForecastRule:
    return ForecastRule(
        id=doc["id"],
        direction=DirectionEnum(doc["direction"]),
        forecast_model=ForecastModelEnum(doc["forecast_model"]),
        volume=Decimal(doc["volume"]),
        lower_bound=Decimal(doc["volume"]),
        upper_bound=Decimal(doc["volume"]),
    )
