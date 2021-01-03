from contextlib import contextmanager

from typing import Optional, List

from PIL import Image
import cv2
import numpy as np
import ffmpeg

from config.config import Config
from components.base_component import BaseComponent


class Playbook:
    def __init__(self, width: int, height: int, number_frames: int, supersample_rate: int = 8):
        self.width = width
        self.height = height
        self.number_frames = number_frames
        self.supersample_rate = supersample_rate
        self.components: List[BaseComponent] = []
        self.current_groups = []

    def _scale_component(self, component: BaseComponent):
        scaling_attributes = component._scaling_attributes()
        for scaling_attribute in scaling_attributes:
            setattr(component, scaling_attribute, getattr(component, scaling_attribute) * self.supersample_rate)

    def add_component(self, component: BaseComponent):
        for group_name in self.current_groups:
            component.add_group(group_name=group_name)
        self._scale_component(component)       
        self.components.append(component)

    def add_transition_to_group(self, transition, group_name: Optional[str] = None):
        transition.scale_attributes(supersample_rate=self.supersample_rate)
        if group_name is None:
            if self.current_groups:
                group_name = self.current_groups[-1]
            else:
                raise ValueError("Only call add_transition_to_group without group_name inside context manager")
        group_components = [component for component in self.components if component.in_group(group_name)]
        for component in group_components:
            component.add_transition(transition)

    @contextmanager
    def with_group(self, group_name):
        self.current_groups.append(group_name)
        yield
        self.current_groups.pop()

    def render(self, filename: str, config: Config):
        process = (
            ffmpeg
            .input('pipe:', format='rawvideo', framerate='60', pix_fmt='rgb24', s='{}x{}'.format(self.width, self.height))
            .output(filename, pix_fmt='yuv420p', crf='1')
            .overwrite_output()
            .run_async(pipe_stdin=True)
        )

        for frame_index in range(self.number_frames):
            image = Image.new('RGB', (self.width * self.supersample_rate, self.height * self.supersample_rate), config.background_color)
            for component in self.components:
                component.render(image, config, frame=frame_index)
            image = image.resize((self.width, self.height))
            # image.save(filename + '_' + str(frame_index) + '.png')
            process.stdin.write(
                cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                .astype(np.uint8)
                .tobytes()
            )

        process.stdin.close()
        process.wait()
