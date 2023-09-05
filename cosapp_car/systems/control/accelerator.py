from cosapp.base import System


class Accelerator(System):
    """Model of a car's accelerator pedal.

    Inputs
    ------
    delta: float,
        pedal angular displacement from rest position

    Outputs
    ------
    w_command: float,
        command signal sent to fuel tank

    """

    def setup(self):

        self.add_inward("delta", 0.0, desc="Pedal angular displacement from rest position", unit="")
        self.add_inward("delta_max", 1.0, desc="Maximum displacement", unit="")

        self.add_outward("w_command", 0.0, desc="command signal", unit="")

    def compute(self):

        self.w_command = self.delta / self.delta_max
