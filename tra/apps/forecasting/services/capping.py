from decimal import Decimal
from typing import Final

from tra.apps.forecasting.services.capping_abc import AbstractForecastCappingService

CAPPING_THRESHOLD: Final[Decimal] = Decimal("50")


class ForecastCappingService(AbstractForecastCappingService):
    """Applies capping logic to forecasting value. If value is over threshold it must be cut."""

    def apply_to(self, forecasting_value: Decimal) -> Decimal:
        if forecasting_value > CAPPING_THRESHOLD:
            return CAPPING_THRESHOLD

        return forecasting_value
