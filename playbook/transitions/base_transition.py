from typing import List, Union

from interpolators.get_interpolator import get_interpolator
from color.color import Color

class BaseTransition:
    def __init__(self, start_values: dict, end_values: dict,
                 start_frame: int, end_frame: int, interpolator: str = 'linear', supersample_scalable: bool = True):
        self.attributes = list(start_values.keys())
        self.start_values = start_values
        self.end_values = end_values
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.supersample_scalable = supersample_scalable
        self.supersample_scaled = False
        self.interpolator = get_interpolator(interpolator)

    def scale_attributes(self, supersample_rate: int):
        if self.supersample_scalable and not self.supersample_scaled:
            self.supersample_scaled = True
            for attribute in self.attributes:
                self.start_values[attribute] *= supersample_rate
                self.end_values[attribute] *= supersample_rate

    def _get_interpolator_value(self, frame: int):
        if frame <= self.start_frame:
            return 0.
        if frame >= self.end_frame:
            return 1.
        return self.interpolator.interpolator_value((frame - self.start_frame) / (self.end_frame - self.start_frame))

    def _apply_attribute_transition(self, start_value, end_value, interpolator_value: float, attribute_type: type):
        if attribute_type == Color:
            return start_value.merge(end_value, interpolator_value)
        if attribute_type == float or attribute_type == int:
            return (1 - interpolator_value) * start_value + interpolator_value * end_value
        raise ValueError(f"Don't understand type {attribute_type}")

    def apply_transition(self, frame: int, current_values: dict, attribute_dict: dict) -> dict:
        return_dict = dict()
        for attribute in self.attributes:
            updated_value = self._apply_attribute_transition(start_value=self.start_values[attribute],
                                                             end_value=self.end_values[attribute],
                                                             interpolator_value=self._get_interpolator_value(frame=frame),
                                                             attribute_type=attribute_dict[attribute]["type"])
            return_dict[attribute] = self.calculate_updated_attribute(current_values[attribute], updated_value)
            if attribute_dict[attribute]["type"] == int:
                return_dict[attribute] = int(round(return_dict[attribute]))
        return return_dict

    def calculate_updated_attribute(self, original_value, updated_value):
        raise NotImplementedError("BaseTransition class")
