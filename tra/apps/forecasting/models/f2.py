from decimal import Decimal

from tra.apps.forecasting.models.abstract import AbstractForecastModel
from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.core.enums import DirectionEnum


class F2ForecastModel(AbstractForecastModel):
    def calculate(self, forecast_rule: ForecastRule) -> Decimal:
        if forecast_rule.direction == DirectionEnum.IN:
            result_volume = forecast_rule.volume * forecast_rule.lower_bound

        else:
            # OUT
            result_volume = forecast_rule.volume * forecast_rule.upper_bound

        return result_volume
