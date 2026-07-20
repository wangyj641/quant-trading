from abc import ABC
from abc import abstractmethod

import pandas as pd


class Strategy(ABC):

    @abstractmethod
    def run(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame: ...
