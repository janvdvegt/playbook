from interpolators.base_interpolator import BaseInterpolator


class LinearInterpolator(BaseInterpolator):
    def interpolator_value(self, linear_value: float):
        return linear_value
