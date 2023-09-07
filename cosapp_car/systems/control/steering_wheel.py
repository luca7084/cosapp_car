from cosapp.base import System

class SteeringWheel(System):
    """Model of a car's steering wheel.

    Inputs
    ------
    angle: float,
        how much the wheel is turned

    Outputs
    ------
    phi: float,
        inclination output

    """
    def setup(self):

        self.add_inward("angle", 0., desc="turning angle of the wheel", unit='')
        self.add_inward("factor", 20., desc="Reduction factor")

        self.add_outward("phi", 0., desc="Inclination command", unit='')

    def compute(self):

        self.phi = self.angle / self.factor