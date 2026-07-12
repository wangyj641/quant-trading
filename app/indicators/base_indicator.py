from abc import ABC
from abc import abstractmethod

import pandas as pd


class Indicator(ABC):

    @abstractmethod
    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        pass
