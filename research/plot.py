import matplotlib.pyplot as plt
import pandas as pd


def plot_price(
    df: pd.DataFrame,
    short_window: int,
    long_window: int,
    trades,
):
    data = df.copy()

    data["short_ma"] = data["close"].rolling(short_window).mean()

    data["long_ma"] = data["close"].rolling(long_window).mean()

    plt.figure(figsize=(14, 7))

    plt.plot(
        data.index,
        data["close"],
        label="Close",
    )

    plt.plot(
        data.index,
        data["short_ma"],
        label=f"MA{short_window}",
    )

    plt.plot(
        data.index,
        data["long_ma"],
        label=f"MA{long_window}",
    )

    buy_label_added = False
    sell_label_added = False

    for trade in trades:

        if not buy_label_added:

            plt.scatter(
                trade.entry_datetime,
                trade.entry_price,
                marker="^",
                s=100,
                label="Buy",
            )

            buy_label_added = True

        else:

            plt.scatter(
                trade.entry_datetime,
                trade.entry_price,
                marker="^",
                s=100,
            )

        if trade.is_closed:

            if not sell_label_added:

                plt.scatter(
                    trade.exit_datetime,
                    trade.exit_price,
                    marker="v",
                    s=100,
                    label="Sell",
                )

                sell_label_added = True

            else:

                plt.scatter(
                    trade.exit_datetime,
                    trade.exit_price,
                    marker="v",
                    s=100,
                )

    plt.title("MU - MA Cross Strategy")

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_equity_curve(
    report,
    benchmark_result,
):

    dates = report.equity_curve.datetimes

    strategy_values = report.equity_curve.values

    benchmark_values = benchmark_result.equity_curve

    plt.figure(figsize=(14, 7))

    plt.plot(
        dates,
        strategy_values,
        label="Strategy",
    )

    plt.plot(
        benchmark_values.index,
        benchmark_values.values,
        label="Buy & Hold",
    )

    plt.title("Strategy vs Buy & Hold")

    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()
