from transitions.base_transition import BaseTransition


class DeltaTransition(BaseTransition):
    def calculate_updated_attribute(self, original_value, updated_value):
        return original_value + updated_value
