from app.database.repository import PriceRepository
from app.indicators.indicator_engine import IndicatorEngine
from app.strategy.ma_cross_strategy import MACrossStrategy
from app.backtest.engine import BacktestEngine
from app.converters.dataframe_converter import DataFrameConverter
from app.execution.backtest_execution import BacktestExecution


class ResearchRunner:

    def run(
        self,
        symbol: str,
        fast: int = 5,
        slow: int = 20,
    ):

        repo = PriceRepository()

        bars = repo.get_history(symbol)

        df = DataFrameConverter.bars_to_dataframe(bars)

        indicator = IndicatorEngine()

        indicator.add_ma(df, fast)
        indicator.add_ma(df, slow)

        df = indicator.calculate(df)

        strategy = MACrossStrategy(
            short_window=5,
            long_window=20,
        )

        # signals = strategy.generate(symbol, df)

        backtest = BacktestEngine(strategy=strategy, initial_cash=10_000)

        report = backtest.run(
            df=df,
            symbol=symbol,
        )

        return df, report
