from cosapp.base import System


class Brakes(System):
    """Model of a car's brake pedal.

    Inputs
    ------
    press: Boolean,
        whether the pedal is being pressed or not

    Outputs
    ------
    lock: Boolean,
        command sent to lock or not

    """

    def setup(self):

        self.add_inward("press", False, desc="whether the pedal is being pressed or not", unit="")

        self.add_outward("lock", False, desc="command to lock", unit="")

    def compute(self):

        self.lock = self.press