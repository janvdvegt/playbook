from PIL import Image

from config.config import Config
from transitions import BaseTransition


class BaseComponent:
    def __init__(self, x: int, y: int, text : str = '', font_size: int = 20, font_color: str = "#000000"):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.groups = []
        self.transitions = []

    def _get_transitionable_attribute_dict(self):
        attributes = self._transitionable_attributes()
        return_dict = dict()
        for attribute in attributes:
            return_dict[attribute] = getattr(self, attribute)
        return return_dict

    def _transitionable_attributes(self):
        return ('x', 'y', 'font_size', 'font_color')

    def _scaling_attributes(self):
        return ('x', 'y', 'font_size')

    def apply_transitions(self, frame: int):
        attribute_values = self._get_transitionable_attribute_dict()
        for transition in self.transitions:
            updated_attribute_values = transition.apply_transition(frame, attribute_values)
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
