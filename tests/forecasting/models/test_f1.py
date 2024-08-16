from decimal import Decimal

import pytest

from tests.factories.forecast_rule import ForecastRuleFactory
from tra.apps.forecasting.models.f1 import F1ForecastModel


class TestF1ForecastModel:
    model_cls = F1ForecastModel

    @pytest.fixture
    def _model(self) -> F1ForecastModel:
        return self.model_cls()

    def test_calculate(self, _model):
        forecast_rule = ForecastRuleFactory(
            volume=Decimal("10"),
            lower_bound=Decimal("5"),
        )

        result = _model.calculate(forecast_rule)

        assert result == Decimal("50")
