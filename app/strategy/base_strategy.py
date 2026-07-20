from abc import ABC
from abc import abstractmethod

import pandas as pd


class Strategy(ABC):

    @abstractmethod
    def generate_signal(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame: ...
