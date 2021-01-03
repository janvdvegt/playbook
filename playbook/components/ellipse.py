from PIL import Image, ImageDraw, ImageFont

from config.config import Config
from components.base_component import BaseComponent
from color.color import Color
from utils import attribute


class Ellipse(BaseComponent):
    @attribute(name="width", type=float, scalable=True)
    @attribute(name="height", type=float, scalable=True)
    @attribute(name="line_width", type=float, scalable=True)
    @attribute(name="fill_color", type=Color, scalable=False)
    @attribute(name="line_color", type=Color, scalable=False)
    def __init__(self, x: int, y: int, width: int, height: int, fill_color, line_color, line_width: int = 1, opacity: float = 1., **kwargs):
        super().__init__(x=x, y=y, opacity=opacity, **kwargs)

    def render(self, image: Image, config: Config, frame: int):
        attribute_values = self.apply_transitions(frame)
        draw = ImageDraw.Draw(image)
        draw.ellipse([(attribute_values['x'] - attribute_values['width'] // 2, attribute_values['y'] - attribute_values['height'] // 2),
                      (attribute_values['x'] + attribute_values['width'] // 2, attribute_values['y'] + attribute_values['height'] // 2)],
                     outline=attribute_values['line_color'].to_tuple(),
                     fill=attribute_values['fill_color'].to_tuple(),
                     width=attribute_values['line_width'])
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", attribute_values['font_size'])
        draw.text(xy=(attribute_values['x'], attribute_values['y']),
                  font=font,
                  text=self.text,
                  fill=attribute_values['font_color'].to_tuple(),
                  anchor='mm')
        image.putalpha(int(round(self.opacity * 255)))
