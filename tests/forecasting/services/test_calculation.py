from decimal import Decimal

from tests.factories.forecast_rule import F1ForecastRuleFactory
from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecasting.model_factory_abc import AbstractForecastModelFactory
from tra.apps.forecasting.models.abstract import AbstractForecastModel
from tra.apps.forecasting.services import ForecastingService
from tra.apps.forecasting.services.capping_abc import AbstractForecastCappingService


class _FakeForecastCappingService(AbstractForecastCappingService):
    def __init__(self) -> None:
        self.applied = False

    def apply_to(self, forecasting_value: Decimal) -> Decimal:
        self.applied = True

        return forecasting_value


_FAKE_FORECASTING_VALUE = Decimal("1")


class _FakeForecastModel(AbstractForecastModel):
    def calculate(self, forecast_rule: ForecastRule) -> Decimal:
        return _FAKE_FORECASTING_VALUE


class _FakeForecastModelFactory(AbstractForecastModelFactory):
    def create(self, forecast_rule: ForecastRule) -> AbstractForecastModel:
        return _FakeForecastModel()


class TestForecastingService:
    service_cls = ForecastingService

    def test_calculate(self):
        forecast_rule = F1ForecastRuleFactory()

        forecasting_service = self.service_cls(
            forecast_model_factory=_FakeForecastModelFactory(),
            capping_service=_FakeForecastCappingService(),
        )

        result = forecasting_service.calculate(forecast_rule)

        assert result == _FAKE_FORECASTING_VALUE

    def test_capping_is_applied(self):
        forecast_rule = F1ForecastRuleFactory()

        capping_service = _FakeForecastCappingService()

        forecasting_service = self.service_cls(
            forecast_model_factory=_FakeForecastModelFactory(),
            capping_service=capping_service,
        )

        forecasting_service.calculate(forecast_rule)

        assert capping_service.applied is True
