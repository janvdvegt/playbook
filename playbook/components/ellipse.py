from PIL import Image, ImageDraw, ImageFont

from config.config import Config
from components.base_component import BaseComponent


class Ellipse(BaseComponent):
    def __init__(self, x: int, y: int, width: int, height: int, fill_color, line_color, line_width: int = 1, **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.fill_color = fill_color
        self.line_color = line_color
        self.width = width
        self.height = height
        self.line_width = line_width

    def _transitionable_attributes(self):
        return super()._transitionable_attributes() + ('fill_color', 'line_color', 'width', 'height', 'line_width')

    def _scaling_attributes(self):
        return super()._scaling_attributes() + ('width', 'height', 'line_width')

    def render(self, image: Image, config: Config, frame: int):
        attribute_values = self.apply_transitions(frame)
        draw = ImageDraw.Draw(image)
        draw.ellipse([(attribute_values['x'] - attribute_values['width'] // 2, attribute_values['y'] - attribute_values['height'] // 2),
                      (attribute_values['x'] + attribute_values['width'] // 2, attribute_values['y'] + attribute_values['height'] // 2)],
                     outline=attribute_values['line_color'],
                     fill=attribute_values['fill_color'],
                     width=attribute_values['line_width'])
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", attribute_values['font_size'])
        draw.text(xy=(attribute_values['x'], attribute_values['y']),
                  font=font,
                  text=self.text,
                  fill=attribute_values['font_color'],
                  anchor='mm')
