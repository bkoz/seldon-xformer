import numpy as np

class DoubleTransformer(object):

   def __init__(self):
       pass

   def transform_input(self, X, feature_names):
       X = np.array(X)
       return X * 2
