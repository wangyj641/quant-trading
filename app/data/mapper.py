from app.database.models import Price

class PriceMapper:

    @staticmethod
    def from_dataframe(
        df,
        symbol,
        interval,
    ):

        prices = []

        for index, row in df.iterrows():
            prices.append(

                Price(
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

        return prices