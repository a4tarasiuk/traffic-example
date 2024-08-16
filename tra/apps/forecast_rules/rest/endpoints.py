from decimal import Decimal

from dependency_injector.wiring import Closing, Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from ulid import ULID

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecast_rules.domain.repositories import AbstractForecastRuleRepository
from tra.apps.forecast_rules.rest.schemas import CreateForecastRuleSchema
from tra.apps.forecasting.services import AbstractForecastingService

FORECAST_RULES_TAG = "forecast-rules"

forecast_rules_router = APIRouter(prefix="/forecast-rules", tags=[FORECAST_RULES_TAG])


@forecast_rules_router.post("")
@inject
def create_forecast_rule(
    rule_schema: CreateForecastRuleSchema,
    *,
    forecast_rule_repository: AbstractForecastRuleRepository = Depends(Provide["forecast_rule_repository"]),
) -> ForecastRule:
    """Creates forecast rule instance."""

    forecast_rule = ForecastRule(
        id=ULID(),
        direction=rule_schema.direction,
        forecast_model=rule_schema.forecast_model,
        volume=rule_schema.volume,
        lower_bound=rule_schema.lower_bound,
        upper_bound=rule_schema.upper_bound,
    )

    forecast_rule = forecast_rule_repository.create(forecast_rule)

    return forecast_rule


@forecast_rules_router.get("")
@inject
def get_forecast_rules(
    *,
    forecast_rule_repository: AbstractForecastRuleRepository = Depends(Closing[Provide["forecast_rule_repository"]]),
) -> tuple[ForecastRule, ...]:
    """Returns full collection of forecast rule instances."""

    forecast_rules = forecast_rule_repository.get_many()

    return forecast_rules


@forecast_rules_router.post("/{forecast_rule_id}/calculate")
@inject
def calculate_forecast_rule(
    forecast_rule_id: ULID,
    *,
    forecast_rule_repository: AbstractForecastRuleRepository = Depends(Closing[Provide["forecast_rule_repository"]]),
    forecasting_service: AbstractForecastingService = Depends(Provide["forecasting_service"]),
) -> Decimal:
    """Performs forecast rule calculation."""

    forecast_rule = forecast_rule_repository.get_by_id(forecast_rule_id)

    if forecast_rule is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    forecasting_value = forecasting_service.calculate(forecast_rule)

    return forecasting_value
