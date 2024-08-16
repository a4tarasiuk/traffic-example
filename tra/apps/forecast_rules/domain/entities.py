from decimal import Decimal

from pydantic import BaseModel
from ulid import ULID

from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.core.enums import DirectionEnum


class ForecastRule(BaseModel):
    id: ULID

    direction: DirectionEnum

    forecast_model: ForecastModelEnum

    volume: Decimal

    lower_bound: Decimal

    upper_bound: Decimal

    def __copy__(self) -> "ForecastRule":
        return ForecastRule(
            id=self.id,
            direction=self.direction,
            forecast_model=self.forecast_model,
            volume=self.volume,
            lower_bound=self.lower_bound,
            upper_bound=self.upper_bound,
        )
