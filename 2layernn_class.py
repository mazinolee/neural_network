import sys, os
sys.path.append(os.pardir)
from common functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:
  def __init__(self, input_size, hidden_size, output_size,
              weight_init_td=0.01)
  self.params = {}
  self.params['W1'] = weight_init_std * \
                      np.random.randn(input_size, hidden_size)
           
