from dataclasses import dataclass

from app.portfolio.portfolio import Portfolio


@dataclass(slots=True)
class ExecutionResult:

    portfolio: Portfolio

    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
