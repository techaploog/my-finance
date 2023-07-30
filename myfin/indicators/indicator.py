from abc import ABC, abstractclassmethod
import pandas as pd

class Indicator(ABC):

    @abstractclassmethod
    def apply(self) -> pd.DataFrame:
        pass