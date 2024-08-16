from factory import Factory, Faker

from tra.apps.forecast_rules.domain.entities import ForecastRule
from tra.apps.forecast_rules.domain.enums import ForecastModelEnum
from tra.core.enums import DirectionEnum


class ForecastRuleFactory(Factory):
    id = Faker("uuid4")

    direction = Faker("random_element", elements=DirectionEnum)

    forecast_model = Faker("random_element", elements=ForecastModelEnum)

    volume = Faker("pydecimal")

    lower_bound = Faker("pydecimal")
    upper_bound = Faker("pydecimal")

    class Meta:
        model = ForecastRule


class InForecastRuleFactory(ForecastRuleFactory):
    direction = DirectionEnum.IN


class OutForecastRuleFactory(ForecastRuleFactory):
    direction = DirectionEnum.OUT
