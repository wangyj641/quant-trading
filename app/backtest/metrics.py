import math

from app.domain.trade import Trade


class BacktestMetrics:

    @staticmethod
    def total_return(
        initial_value: float,
        final_value: float,
    ) -> float:

        if initial_value == 0:
            return 0.0

        return (final_value - initial_value) / initial_value

    @staticmethod
    def max_drawdown(
        equity_values: list[float],
    ) -> float:

        if not equity_values:
            return 0.0

        peak = equity_values[0]
        max_drawdown = 0.0

        for equity in equity_values:

            peak = max(
                peak,
                equity,
            )

            drawdown = (equity - peak) / peak

            max_drawdown = min(
                max_drawdown,
                drawdown,
            )

        return max_drawdown

    @staticmethod
    def volatility(
        equity_values: list[float],
        periods_per_year: int = 252,
    ) -> float:

        if len(equity_values) < 2:
            return 0.0

        returns = []

        for i in range(1, len(equity_values)):

            previous = equity_values[i - 1]
            current = equity_values[i]

            if previous == 0:
                continue

            returns.append(current / previous - 1)

        if len(returns) < 2:
            return 0.0

        mean = sum(returns) / len(returns)

        variance = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)

        return math.sqrt(variance) * math.sqrt(periods_per_year)

    @staticmethod
    def sharpe_ratio(
        equity_values: list[float],
        risk_free_rate: float = 0.0,
        periods_per_year: int = 252,
    ) -> float:

        if len(equity_values) < 2:
            return 0.0

        returns = []

        for i in range(1, len(equity_values)):

            previous = equity_values[i - 1]
            current = equity_values[i]

            if previous == 0:
                continue

            returns.append(current / previous - 1)

        if len(returns) < 2:
            return 0.0

        daily_rf = risk_free_rate / periods_per_year

        excess_returns = [r - daily_rf for r in returns]

        mean = sum(excess_returns) / len(excess_returns)

        variance = sum((r - mean) ** 2 for r in excess_returns) / (
            len(excess_returns) - 1
        )

        std = math.sqrt(variance)

        if std == 0:
            return 0.0

        return (mean / std) * math.sqrt(periods_per_year)

    @staticmethod
    def gross_profit(
        trades: list[Trade],
    ) -> float:

        return sum(trade.pnl for trade in trades if trade.is_winner)

    @staticmethod
    def gross_loss(
        trades: list[Trade],
    ) -> float:

        return sum(-trade.pnl for trade in trades if trade.is_loser)

    @staticmethod
    def win_rate(
        trades: list[Trade],
    ) -> float:

        if not trades:
            return 0.0

        winners = sum(1 for trade in trades if trade.is_winner)

        return winners / len(trades)

    @staticmethod
    def profit_factor(
        trades: list[Trade],
    ) -> float:

        gross_profit = BacktestMetrics.gross_profit(trades)

        gross_loss = BacktestMetrics.gross_loss(trades)

        if gross_loss == 0:

            if gross_profit > 0:
                return float("inf")

            return 0.0

        return gross_profit / gross_loss
