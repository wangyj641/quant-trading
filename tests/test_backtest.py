import pandas as pd

from app.backtest.engine import BacktestEngine
from app.backtest.metrics import Metrics
from app.domain.signal import SignalType
from app.execution.backtest_execution import BacktestExecution
from app.execution.base import ExecutionResult
from app.execution.backtest_execution import BacktestExecution


def test_backtest():

    execution_engine = BacktestExecution(initial_cash=100000)

    backtest = BacktestEngine(execution_engine)

    assert isinstance(backtest, BacktestEngine)
