import numpy as np


def get_shape(array):
    """
    image: object from PIL.image.open
    """
    
    return np.frombuffer(array).size