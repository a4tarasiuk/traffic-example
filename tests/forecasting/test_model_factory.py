import pytest

from tests.factories.forecast_rule import F1ForecastRuleFactory, F2ForecastRuleFactory, ForecastRuleFactory
from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.apps.forecasting.model_factory import ForecastModelFactory
from tra.apps.forecasting.models.f1 import F1ForecastModel
from tra.apps.forecasting.models.f2 import F2ForecastModel


class TestModelFactory:
    model_factory_cls = ForecastModelFactory

    @pytest.mark.parametrize("rule_factory,rule_model_cls", [
        (F1ForecastRuleFactory, F1ForecastModel),
        (F2ForecastRuleFactory, F2ForecastModel),
    ])
    def test_create(self, rule_factory, rule_model_cls):
        rule = rule_factory()

        model_factory = self.model_factory_cls()

        model = model_factory.create(rule)

        assert isinstance(model, rule_model_cls)

    def test_when_model_is_not_supported(self):
        rule = ForecastRuleFactory(forecast_model=ForecastModelEnum.F3)

        model_factory = self.model_factory_cls()

        with pytest.raises(ValueError) as exc_info:
            model_factory.create(rule)

        assert "is not supported" in exc_info.value.args[0]
