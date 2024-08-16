import dataclasses
from datetime import date
from typing import Iterator

from dateutil.relativedelta import relativedelta
from dateutil.rrule import MONTHLY, rrule


@dataclasses.dataclass
class DatePeriod:
    start_date: date
    end_date: date

    def __init__(self, start_date: date, end_date: date) -> None:
        self.start_date = start_date.replace(day=1)
        self.end_date = end_date + relativedelta(day=31)

    @classmethod
    def create_from_month(cls, month: date) -> "DatePeriod":
        return DatePeriod(month, month)

    def __copy__(self) -> "DatePeriod":
        return DatePeriod(self.start_date, self.end_date)

    def __iter__(self) -> Iterator["Month"]:
        for dt in rrule(freq=MONTHLY, dtstart=self.start_date, until=self.end_date):
            yield Month.create_from_date(dt.date())

    @property
    def period(self) -> tuple[date, date]:
        return self.start_date, self.end_date


class Month(date):
    @classmethod
    def create_from_date(cls, v: date) -> "Month":
        return cls(v.year, v.month, day=1)

    @classmethod
    def create_from_year_month(cls, year: int, month: int) -> "Month":
        return cls(year, month, day=1)

    def to_date(self) -> date:
        return date(self.year, self.month, self.day)
