import numpy as np


def get_size(array):
    """
    image: object from PIL.image.open
    """
    
    return np.frombuffer(array).size