from PIL import Image, ImageDraw, ImageFont

from config.config import Config
from components.base_component import BaseComponent
from utils import attribute


class Rectangle(BaseComponent):
    @attribute(name="width", type=float, scalable=True)
    @attribute(name="height", type=float, scalable=True)
    @attribute(name="line_width", type=float, scalable=True)
    @attribute(name="fill_color", type="color", scalable=False)
    @attribute(name="line_color", type="color", scalable=False)
    def __init__(self, x: int, y: int, width: int, height: int, fill_color, line_color, line_width: int = 1, **kwargs):
        super().__init__(x=x, y=y, **kwargs)
    
    def render(self, image: Image, config: Config, frame: int):
        attribute_values = self.apply_transitions(frame)
        draw = ImageDraw.Draw(image)
        draw.rectangle([(attribute_values['x'] - attribute_values['width'] // 2, attribute_values['y'] - attribute_values['height'] // 2),
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
