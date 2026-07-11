from app.database.models import Price


class ORMMapper:

    @staticmethod
    def to_price(bar):

        return Price(
            symbol=bar.symbol,
            datetime=bar.datetime,
            interval=bar.interval,
            open=bar.open,
            high=bar.high,
            low=bar.low,
            close=bar.close,
            volume=bar.volume,
        )
