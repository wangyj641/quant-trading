from app.database.models import Price
from app.domain.market_bar import MarketBar


class PriceMapper:

    @staticmethod
    def from_dataframe(
        df,
        symbol,
        interval,
    ):

        bars = []

        for index, row in df.iterrows():
            bars.append(
                MarketBar(
                    symbol=symbol,
                    datetime=index.to_pydatetime(),
                    interval=interval,
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=float(row["Volume"]),
                )
            )
        return bars
