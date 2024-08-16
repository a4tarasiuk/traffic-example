from decimal import Decimal

from pydantic import BaseModel

from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.core.enums import DirectionEnum


class CreateForecastRuleSchema(BaseModel):
    direction: DirectionEnum

    forecast_model: ForecastModelEnum

    volume: Decimal

    lower_bound: Decimal

    upper_bound: Decimal
