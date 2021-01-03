from typing import Optional

class Color:
    def __init__(self, raw_color=None, r=None, g=None, b=None):
        self.r, self.g, self.b = r, g, b
        if raw_color:
            self.translate_color(raw_color)

    def translate_color(self, raw_color):
        if isinstance(raw_color, str):
            self.r = int(raw_color[1:3], 16)
            self.g = int(raw_color[3:5], 16)
            self.b = int(raw_color[5:7], 16)
        elif isinstance(raw_color, Color):
            self.r = raw_color.r
            self.g = raw_color.g
            self.b = raw_color.b

    def to_tuple(self, opacity: Optional[float] = None):
        if opacity is not None:
            return self.r, self.g, self.b, int(round(opacity * 255))
        return self.r, self.g, self.b

    def merge(self, other_color, mixture: float):
        return Color(r=int(round((1 - mixture) * self.r + mixture * other_color.r)),
                     g=int(round((1 - mixture) * self.g + mixture * other_color.g)),
                     b=int(round((1 - mixture) * self.b + mixture * other_color.b)))
