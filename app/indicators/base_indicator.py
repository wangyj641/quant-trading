from abc import ABC
from abc import abstractmethod

import pandas as pd


class Indicator(ABC):

    @property
    @abstractmethod
    def column_name(self) -> str: ...

    @abstractmethod
    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.Series: ...
