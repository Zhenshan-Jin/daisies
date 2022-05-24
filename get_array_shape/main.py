import numpy as np
import pandas as pd


def get_size(array:pd.DataFrame):
    """
    image: object from PIL.image.open
    
    :param array: here are some addtional comment
    """
    with open(array, "rb") as istr:
        arr = np.frombuffer(istr.read())
    return arr.size


