from PIL import ImageColor

from playbook import Playbook
from components.rectangle import Rectangle
from components.ellipse import Ellipse
from transitions import DeltaTransition, MultiplicativeTransition

from config.config import Config

background_color = "#EAF6FF"
primary_color = "#2A2A72"
secondary_color = "#232528"

config = Config(primary_color=primary_color, secondary_color=secondary_color, background_color=background_color)

playbook = Playbook(width=800, height=600, number_frames=51)

with playbook.with_group("rectangles"):
    for x in range(3):
        for y in range(3):
            rectangle = Rectangle(x=150 + x * 100, y=150 + y * 100, width=90, height=90, line_width=3,
                                  fill_color=config.primary_color, line_color=config.secondary_color,
                                  text=f"({x},{y})", font_size=40, font_color="#ffffff")
            playbook.add_component(rectangle)
    playbook.add_transition_to_group(DeltaTransition(start_values={'x': 0, 'y': 0},
                                                     end_values={'x': -50, 'y': -50},
                                                     start_frame=1, end_frame=50,
                                                     interpolator='sigmoid'))
    playbook.add_transition_to_group(MultiplicativeTransition(start_values={'width': 1., 'height': 1., 'x': 1.0, 'y': 1.0},
                                                              end_values={'width': 0.5, 'height': 0.5, 'x': 0.5, 'y': 0.5},
                                                              start_frame=1, end_frame=50,
                                                              interpolator='sigmoid',
                                                              supersample_scalable=False))

playbook.render('test.mp4', config=config)
