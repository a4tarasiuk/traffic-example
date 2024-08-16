from decimal import Decimal

from tra.apps.forecasting.models.abstract import AbstractForecastModel
from tra.apps.forecast_rules.domain.entities import ForecastRule


class F1ForecastModel(AbstractForecastModel):
    def calculate(self, forecast_rule: ForecastRule) -> Decimal:
        return forecast_rule.volume * forecast_rule.lower_bound
