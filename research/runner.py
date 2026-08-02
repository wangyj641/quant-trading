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

    def load_data(
        self,
        symbol: str,
        timeframe: TimeFrame,
    ):

        df = self.repository.get_history(
            symbol=symbol,
            timeframe=timeframe,
        )

        if df.empty:
            raise ValueError(f"No historical data found for {symbol}")

        return df

    def run(
        self,
        symbol: str,
        strategy: Strategy,
        timeframe: TimeFrame = TimeFrame.DAY_1,
        initial_cash: float = 100_000,
    ):

        df = self.load_data(
            symbol=symbol,
            timeframe=timeframe,
        )

        engine = BacktestEngine(
            strategy=strategy,
            initial_cash=initial_cash,
        )

        return engine.run(
            df=df,
            symbol=symbol,
        )
