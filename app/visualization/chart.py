import matplotlib.pyplot as plt


class Chart:

    @staticmethod
    def plot_price(df, signals):

        plt.figure(figsize=(16, 8))

        plt.plot(
            df.index,
            df["close"],
            label="Close",
        )

        plt.plot(
            df.index,
            df["MA5"],
            label="MA5",
        )

        plt.plot(
            df.index,
            df["MA20"],
            label="MA20",
        )

        buy = df[df["signal"] == 1]

        plt.scatter(
            buy.index,
            buy["close"],
            marker="^",
            s=120,
            label="BUY",
        )

        sell = df[df["signal"] == -1]

        plt.scatter(
            sell.index,
            sell["close"],
            marker="v",
            s=120,
            label="SELL",
        )

        plt.legend()

        plt.grid(True)

        plt.show()

        plt.savefig(
            "report.png",
            dpi=300,
        )
