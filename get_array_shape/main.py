import numpy as np
import pandas as pd


def get_size(array:pd.DataFrame):
    """
    image: object from PIL.image.open
    """
    with open(array, "rb") as istr:
        arr = np.frombuffer(istr.read())
    return arr.size