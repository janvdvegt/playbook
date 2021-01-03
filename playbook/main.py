from PIL import ImageColor

from playbook import Playbook
from components import Rectangle, Ellipse, Text
from transitions import DeltaTransition, MultiplicativeTransition, AbsoluteTransition
from color.color import Color

from config.config import Config

background_color = Color("#EAF6FF")
primary_color = Color("#2A2A72")
primary_color_highlight = Color("#8F8F72")
secondary_color = Color("#232528")

config = Config(primary_color=primary_color, secondary_color=secondary_color, background_color=background_color)

playbook = Playbook(width=1920, height=1080, number_frames=51, supersample_rate=1)

with playbook.with_group("rectangles"):
    for x in range(3):
        for y in range(3):
            rectangle = Rectangle(x=150 + x * 100, y=150 + y * 100, width=90, height=90, line_width=3,
                                  fill_color=config.primary_color, line_color=config.secondary_color,
                                  text=f"({x},{y})", font_size=25, font_color="#ffffff", opacity=1.)
            if (x + y) % 2 == 0:
                rectangle.add_group("even")
            playbook.add_component(rectangle)
    playbook.add_transition_to_group(DeltaTransition(start_values={'x': 0, 'y': 0},
                                                     end_values={'x': -50, 'y': -50},
                                                     start_frame=1, end_frame=50,
                                                     interpolator='sigmoid'))
    playbook.add_transition_to_group(MultiplicativeTransition(start_values={'width': 1., 'height': 1., 'x': 1.0, 'y': 1.0, 'font_size': 1.0, 'opacity': 1.0},
                                                              end_values={'width': 0.5, 'height': 0.5, 'x': 0.5, 'y': 0.5, 'font_size': 0.5, 'opacity': 0.2},
                                                              start_frame=1, end_frame=50,
                                                              interpolator='sigmoid',
                                                              supersample_scalable=False))

playbook.add_transition_to_group(AbsoluteTransition(start_values={'fill_color': primary_color},
                                                    end_values={'fill_color': primary_color_highlight},
                                                    start_frame=21, end_frame=50,
                                                    supersample_scalable=False),
                                 group_name="even")

text = Text(x=800, y=300, text="TEST TEST", font_size=80, font_color=Color("#000000"), opacity=0.)
playbook.add_component(text)
text.add_transition(DeltaTransition(start_values={'opacity': 0.},
                                    end_values={'opacity': 1.0},
                                    start_frame=20, end_frame=40,
                                    interpolator='sigmoid'))

playbook.render('test.mp4', config=config)
