import numpy as np

from interpolators.base_interpolator import BaseInterpolator


class SigmoidInterpolator(BaseInterpolator):
    def interpolator_value(self, linear_value: float):
        sigmoid_input_value = linear_value * 12 - 6
        return np.exp(sigmoid_input_value) / (np.exp(sigmoid_input_value) + 1)
