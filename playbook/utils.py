from functools import wraps
from color.color import Color

def attribute(name: str, type, scalable: bool):
    def decorator(func):
        @wraps(func)
        def __init__(self, *args, **kwargs):
            if type == Color:
                value = Color(raw_color=kwargs[name])
            else:
                value = kwargs[name]
            setattr(self, name, value)
            func(self, *args, **kwargs)
            self._register_attribute(name=name, type=type, scalable=scalable)
        return __init__
    return decorator
