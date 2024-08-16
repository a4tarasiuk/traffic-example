from dataclasses import dataclass
from decimal import Decimal

from tra.apps.forecast_rules.domain.enums import ForecastDistributionModelEnum, ForecastModelEnum
from tra.core.enums import DirectionEnum
from tra.core.types import DatePeriod


@dataclass
class ForecastRule:
    id: str

    hpmns: tuple[str, ...]

    direction: DirectionEnum

    period: DatePeriod

    forecast_model: ForecastModelEnum

    distribution_model: ForecastDistributionModelEnum

    volume: Decimal

    def __copy__(self) -> "ForecastRule":
        return ForecastRule(
            id=self.id,
            hpmns=self.hpmns,
            direction=self.direction,
            period=self.period,
            forecast_model=self.forecast_model,
            distribution_model=self.distribution_model,
            volume=self.volume,
        )
