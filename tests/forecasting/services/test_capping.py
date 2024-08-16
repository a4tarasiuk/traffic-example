from decimal import Decimal

from tra.apps.forecasting.services.capping import CAPPING_THRESHOLD, ForecastCappingService


class TestForecastCappingService:
    service_cls = ForecastCappingService

    def test_when_input_value_over_threshold(self):
        forecasting_value = CAPPING_THRESHOLD + Decimal("10")

        capped_forecasting_value = self.service_cls().apply_to(forecasting_value)

        assert capped_forecasting_value == CAPPING_THRESHOLD

    def test_when_input_value_below_threshold(self):
        forecasting_value = CAPPING_THRESHOLD - Decimal("10")

        capped_forecasting_value = self.service_cls().apply_to(forecasting_value)

        assert capped_forecasting_value == forecasting_value
