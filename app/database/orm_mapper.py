from app.database.models import Price
from app.domain.market_bar import MarketBar


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

    @staticmethod
    def to_market_bar(price: Price):

        return MarketBar(
            symbol=price.symbol,
            datetime=price.datetime,
            interval=price.interval,
            open=price.open,
            high=price.high,
            low=price.low,
            close=price.close,
            volume=price.volume,
        )
