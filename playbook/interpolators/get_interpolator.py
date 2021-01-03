from interpolators.linear_interpolator import LinearInterpolator
from interpolators.sigmoid_interpolator import SigmoidInterpolator


def get_interpolator(interpolator: str):
    if interpolator == "linear":
        return LinearInterpolator()
    if interpolator == 'sigmoid':
        return SigmoidInterpolator()
    raise ValueError(f"Don't know interpolator {interpolator}")
