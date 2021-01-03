from PIL import Image

from config.config import Config
from transitions import BaseTransition
from utils import attribute


class BaseComponent:
    @attribute(name='x', type=float, scalable=True)
    @attribute(name='y', type=float, scalable=True)
    @attribute(name='font_size', type=int, scalable=True)
    @attribute(name='font_color', type="color", scalable=False)
    def __init__(self, x: int, y: int, text: str = '', font_size: int = 20, font_color: str = "#000000", **kwargs):
        self.text = text
        self.groups = []
        self.transitions = []
        self.attribute_dict = {}

    def _register_attribute(self, name, type, scalable=True):
        self.attribute_dict[name] = {'type': type, 'scalable': scalable}

    def _get_transitionable_attribute_dict(self):
        attributes = self._transitionable_attributes()
        return_dict = dict()
        for attribute in attributes:
            return_dict[attribute] = getattr(self, attribute)
        return return_dict

    def _transitionable_attributes(self):
        return list(self.attribute_dict.keys())

    def _scaling_attributes(self):
        return [key for key in self.attribute_dict.keys() if self.attribute_dict[key]["scalable"]]

    def apply_transitions(self, frame: int):
        attribute_values = self._get_transitionable_attribute_dict()
        for transition in self.transitions:
            updated_attribute_values = transition.apply_transition(frame, attribute_values, self.attribute_dict)
            attribute_values.update(updated_attribute_values)
        return attribute_values

    def in_group(self, group_name: str):
        return group_name in self.groups

    def add_group(self, group_name: str):
        self.groups.append(group_name)

    def add_transition(self, transition: BaseTransition):
        self.transitions.append(transition)
    
    def render(self, image: Image, config: Config, frame: int):
        raise NotImplementedError("Base Component class")
