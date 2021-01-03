from PIL import Image, ImageDraw, ImageFont

from config.config import Config
from components.base_component import BaseComponent


class Rectangle(BaseComponent):
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
        x, y, width, height, line_width, font_size = self.apply_transitions(frame) 
        draw = ImageDraw.Draw(image)
        draw.rectangle([(x - width // 2, y - height // 2), (x + width // 2, y + height // 2)],
                        outline=self.line_color,
                        fill=self.fill_color,
                        width=line_width)
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", font_size)
        draw.text(xy=(x, y),
                  font=font,
                  text=self.text,
                  fill=self.font_color,
                  anchor='mm')
