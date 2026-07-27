from app.database.repository import PriceRepository
from app.indicators.indicator_engine import IndicatorEngine
from app.strategy.ma_cross_strategy import MACrossStrategy
from app.backtest.engine import BacktestEngine
from app.domain.timeframe import TimeFrame
from app.indicators.ma_indicator import MAIndicator
from app.converters.dataframe_converter import DataFrameConverter
from app.execution.backtest_execution import BacktestExecution
from app.portfolio.portfolio import Portfolio


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

        strategy = MACrossStrategy()

        signals = strategy.generate(symbol, df)

        portfolio = Portfolio(100000)

        execution_engine = BacktestExecution(initial_cash=100000)

        backtest = BacktestEngine(execution_engine)

        report = backtest.run(
            df=df,
            signals=signals,
        )

        return df, signals, report
