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

playbook = Playbook(width=800, height=600, number_frames=60)

with playbook.with_group("rectangles"):
    first_rectangle = Ellipse(x=150, y=100, width=300, height=200, line_width=3,
                                fill_color=config.primary_color, line_color=config.secondary_color,
                                text="Dzy", font_size=80, font_color="#ffffff")

    second_rectangle = Ellipse(x=225, y=225, width=400, height=400, line_width=5,
                                fill_color=config.primary_color, line_color=config.secondary_color,
                                text="Dzy", font_size=80, font_color="#ffffff")
    playbook.add_component(first_rectangle)
    playbook.add_component(second_rectangle)
    playbook.add_transition_to_group(DeltaTransition(start_values={'x': 0, 'y': 0},
                                                     end_values={'x': 100, 'y': 100},
                                                     start_frame=1, end_frame=50,
                                                     interpolator='sigmoid'))
    playbook.add_transition_to_group(MultiplicativeTransition(start_values={'width': 1., 'height': 1.},
                                                              end_values={'width': 0.5, 'height': 0.5},
                                                              start_frame=1, end_frame=50,
                                                              interpolator='sigmoid',
                                                              supersample_scalable=False))
    
    # playbook.add_transition_to_group(transition=TranslationTransition(x_delta=100, y_delta=100, start_frame=1, end_frame=5))
    # playbook.add_transition_to_group(transition=ResizeTransition(multiplier_from=1, multiplier_to=0.5, start_frame=1, end_frame=5))

circle = Ellipse(x=400, y=400, width=250, height=250, line_width=10,
                 fill_color=config.secondary_color, line_color="#ff0000",
                 text="Dzy", font_size=40, font_color="#ffffff")
# circle.add_transition(ResizeTransition(multiplier_from=1, multiplier_to=2, start_frame=3, end_frame=100))

playbook.add_component(circle)
playbook.render('test.mp4', config=config)
