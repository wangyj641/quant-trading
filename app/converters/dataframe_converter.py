from __future__ import annotations

import pandas as pd

from app.domain.market_bar import MarketBar


class DataFrameConverter:

    @staticmethod
    def bars_to_dataframe(
        bars: list[MarketBar],
    ) -> pd.DataFrame:

        data = []

        for bar in bars:

            data.append(
                {
                    "datetime": bar.datetime,
                    "open": bar.open,
                    "high": bar.high,
                    "low": bar.low,
                    "close": bar.close,
                    "volume": bar.volume,
                }
            )

        df = pd.DataFrame(data)

        if df.empty:
            return df

        df = df.sort_values("datetime")

        df = df.set_index("datetime")

        return df
