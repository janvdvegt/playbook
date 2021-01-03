from PIL import Image, ImageDraw, ImageFont

from config.config import Config
from components.base_component import BaseComponent
from color.color import Color
from utils import attribute


class Text(BaseComponent):
    def __init__(self, x: int, y: int, opacity: float = 1., **kwargs):
        super().__init__(x=x, y=y, opacity=opacity, **kwargs)
    
    def render(self, image: Image, config: Config, frame: int):
        attribute_values = self.apply_transitions(frame)
        print(attribute_values["opacity"])
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", attribute_values['font_size'])
        draw.text(xy=(attribute_values['x'], attribute_values['y']),
                  font=font,
                  text=self.text,
                  fill=attribute_values['font_color'].to_tuple(opacity=attribute_values["opacity"]),
                  anchor='mm')
