from abc import ABC, abstractclassmethod
import pandas as pd

class Indicator(ABC):

    @abstractclassmethod
    def apply(self) -> pd.DataFrame:
        pass

    
    def get_df (self,serie:pd.Series | pd.DataFrame, column:str):
        data = None

        if (isinstance(serie,pd.Series)):
            data = serie.copy()
            data = pd.DataFrame(data)
        elif (isinstance(serie,pd.DataFrame)) :
            data = serie[[column]].copy()
        
        
        return data