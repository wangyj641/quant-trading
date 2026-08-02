from app.backtest.engine import BacktestEngine
from app.database.repository import PriceRepository
from app.strategy.base_strategy import Strategy
from app.domain.timeframe import TimeFrame


class ResearchRunner:

    def __init__(
        self,
        repository: PriceRepository,
    ):
        self.repository = repository

    def run(
        self,
        symbol: str,
        strategy: Strategy,
        timeframe: TimeFrame = TimeFrame.DAY_1,
        initial_cash: float = 100_000,
    ):

        # 1. Load historical data
        df = self.repository.get_history(
            symbol=symbol,
            timeframe=timeframe,
        )

        if df.empty:
            raise ValueError(f"No historical data found for {symbol}")

        # 2. Create backtest engine
        engine = BacktestEngine(
            strategy=strategy,
            initial_cash=initial_cash,
        )

        # 3. Run backtest
        report = engine.run(
            df=df,
            symbol=symbol,
        )

        return report
