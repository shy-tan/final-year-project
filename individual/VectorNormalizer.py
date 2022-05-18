import pandas as pd
import numpy as np
from typing import List

class VectorNormalizer:
    """
    provided methods to fit, transform and inverse transform 2-D arrays 
    transformation applied: x/ L2 norm of X =>
    """
    def __init__(self) -> None:
        """
        intialize attributes
        """
        self.norms = []
        self.inverse_transformed = []
        self.transformed = []

    def fit(self, dataframe) -> List[int]:
        """
        calculates norms of all row vectors in the dataframe

        returns: list of norms
        """
        for item in dataframe.to_numpy():
            self.norms.append(np.sqrt(np.sum(np.square(item))))
        
        return self.norms

    def transform(self, dataframe) -> pd.DataFrame():
        """
        performs vector normalization

        returns: original dataframe after normalization
        """        
        for idx, item in enumerate(dataframe.to_numpy()):
            self.transformed.append(item/self.norms[idx])
        
        return pd.DataFrame(self.transformed)


    def inverse_transform(self, inverse_transformed_df) -> pd.DataFrame():
        """
        calculates product of norms of all row vectors with row vectors in the dataframe

        returns: original dataframe after transformations
        
        """
        for idx, item in enumerate(inverse_transformed_df.to_numpy()):
            self.inverse_transformed.append(item * self.norms[idx])
        
        return pd.DataFrame(self.inverse_transformed)