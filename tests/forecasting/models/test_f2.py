from decimal import Decimal

import pytest

from tests.factories.forecast_rule import InForecastRuleFactory, OutForecastRuleFactory
from tra.apps.forecasting.models.f2 import F2ForecastModel


class TestF2ModelFactory:
    model_cls = F2ForecastModel

    @pytest.fixture
    def _model(self):
        return self.model_cls()

    def test_when_direction_is_in(self, _model):
        rule = InForecastRuleFactory(volume=Decimal("50"), lower_bound=Decimal("10"))

        result = _model.calculate(rule)

        assert result == Decimal("500")

    def test_when_direction_is_out(self, _model):
        rule = OutForecastRuleFactory(volume=Decimal("50"), upper_bound=Decimal("5"))

        result = _model.calculate(rule)

        assert result == Decimal("250")
