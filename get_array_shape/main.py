import numpy as np
import pandas as pd


def get_size(array:pd.DataFrame):
    """
    image: object from PIL.image.open
    """
    
    return np.load(array, allow_pickle=True).size