from research.runner import ResearchRunner
from app.utils.logger import logger
from app.backtest.report_formatter import ReportFormatter

runner = ResearchRunner()

df, signals, report = runner.run(
    symbol="MU",
    fast=5,
    slow=20,
)

logger.info(f"The report is:")

ReportFormatter.print(report)
