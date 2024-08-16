from abc import ABC
from decimal import Decimal


class AbstractForecastCappingService(ABC):
    """Interface that represents application of limits/thresholds for forecasting result value."""

    def apply_to(self, forecasting_value: Decimal) -> Decimal:
        """Applies capping rule for forecasting value."""
