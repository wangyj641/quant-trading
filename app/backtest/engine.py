from app.execution.base import ExecutionResult


class BacktestEngine:

    def __init__(
        self,
        execution_engine,
    ):
        self.execution_engine = execution_engine

    def run(
        self,
        df,
        signals,
    ) -> ExecutionResult:

        result = self.execution_engine.execute(
            df=df,
            signals=signals,
        )

        return result
