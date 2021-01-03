from transitions.base_transition import BaseTransition


class MultiplicativeTransition(BaseTransition):
    def _apply_attribute_transition(self, start_value, end_value, interpolator_value: float):
        return (1 - interpolator_value) * start_value + interpolator_value * end_value

    def calculate_updated_attribute(self, original_value, updated_value):
        return original_value * updated_value
