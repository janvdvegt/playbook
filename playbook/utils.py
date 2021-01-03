from functools import wraps

def attribute(name: str, type, scalable: bool):
    def decorator(func):
        @wraps(func)
        def __init__(self, *args, **kwargs):
            setattr(self, name, kwargs[name])
            func(self, *args, **kwargs)
            self._register_attribute(name=name, type=type, scalable=scalable)
        return __init__
    return decorator
