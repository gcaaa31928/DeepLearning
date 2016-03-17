import numpy as np
class Tool():

    @classmethod
    def sigmoid(cls, t):
        return 1/(1+np.exp(t))

