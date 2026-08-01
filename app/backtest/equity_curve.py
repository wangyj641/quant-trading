from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class EquityPoint:
    datetime: datetime
    equity: float


class EquityCurve:

    def __init__(self):
        self.points: list[EquityPoint] = []

    def add(
        self,
        datetime: datetime,
        equity: float,
    ) -> None:

        self.points.append(
            EquityPoint(
                datetime=datetime,
                equity=equity,
            )
        )

    @property
    def values(self) -> list[float]:
        return [point.equity for point in self.points]

    @property
    def datetimes(self) -> list[datetime]:
        return [point.datetime for point in self.points]

    @property
    def initial_value(self) -> float:
        if not self.points:
            return 0.0

        return self.points[0].equity

    @property
    def final_value(self) -> float:
        if not self.points:
            return 0.0

        return self.points[-1].equity
