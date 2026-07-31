from app.backtest import report


class ReportFormatter:

    @staticmethod
    def print(report):

        print("=" * 40)

        print(f"Initial Cash : {report.initial_cash:,.2f}")

        print(f"Final Cash   : {report.final_cash:,.2f}")

        print(f"Return       : {report.total_return:.2%}")

        print("Trades:")
        if report.trades:
            for trade in report.trades:
                trade.print()
        else:
            print("  No trades executed")

        print("=" * 40)
