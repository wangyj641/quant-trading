from app.database.repository import PriceRepository
from app.indicators.indicator_engine import IndicatorEngine
from app.strategy.ma_cross_strategy import MACrossStrategy
from app.backtest.engine import BacktestEngine
from app.domain.timeframe import TimeFrame
from app.indicators.ma_indicator import MAIndicator
from app.converters.dataframe_converter import DataFrameConverter
from app.execution.backtest_execution import BacktestExecution
from app.portfolio.portfolio import Portfolio


def main():
    repo = PriceRepository()

    bars = repo.get_history(
        symbol="MU",
        timeFrame=TimeFrame.DAY_1,
        limit=1000,
    )

    df = DataFrameConverter.bars_to_dataframe(bars)

    engine = IndicatorEngine()

    engine.register(MAIndicator(5))
    engine.register(MAIndicator(20))

    df = engine.calculate(df)

    strategy = MACrossStrategy()

    signals = strategy.generate("MU", df)

    portfolio = Portfolio(100000)

    execution_engine = BacktestExecution(initial_cash=100000)

    backtest = BacktestEngine(execution_engine)

    result = backtest.run(df, signals)


if __name__ == "__main__":
    main()
