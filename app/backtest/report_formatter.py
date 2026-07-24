class ReportFormatter:

    @staticmethod
    def print(report):

        print("=" * 40)

        print(f"Initial Cash : {report.initial_cash:,.2f}")

        print(f"Final Cash   : {report.final_cash:,.2f}")

        print(f"Return       : {report.total_return:.2%}")

        print(f"Trades       : {report.trade_count}")

        print(f"Win Rate     : {report.win_rate:.2%}")

        print(f"Max DD       : {report.max_drawdown:.2%}")

        print("=" * 40)
