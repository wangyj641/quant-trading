import matplotlib.pyplot as plt


def plot_equity_curve(report):

    plt.figure(figsize=(12, 6))

    plt.plot(report.equity_curve.index, report.equity_curve.values)

    plt.title("Equity Curve")

    plt.xlabel("Date")

    plt.ylabel("Portfolio Value")

    plt.grid()

    plt.show()
