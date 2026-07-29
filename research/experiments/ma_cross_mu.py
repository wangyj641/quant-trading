from research.runner import ResearchRunner
from app.utils.logger import logger

runner = ResearchRunner()

df, signals, report = runner.run(
    symbol="MU",
    fast=5,
    slow=20,
)

logger.info(f"ma cross MU")

# ReportFormatter.print(report)
