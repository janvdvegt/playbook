from transitions.base_transition import BaseTransition


class AbsoluteTransition(BaseTransition):
    def calculate_updated_attribute(self, original_value, updated_value):
        return updated_value
