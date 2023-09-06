from cosapp.base import System


class Wheels(System):
    """Simple model of a set of 4 wheels.

    Inputs
    ------
    M [N*m]: float,
        torque

    Outputs
    ------
    omega [1/s]: float,
        wheels' angular speed
    weight [kg]: float,
        weight
    force [N]: float,
        friction force acting over the wheels

    """

    def setup(self):

        # Geometric parameters
        self.add_inward("R", 2.0, desc="Wheel radius", unit="m")
        self.add_inward("mw", 1.0, desc="Wheel mass", unit="kg")

        # inputs
        self.add_inward("M", 0.0, desc="External torque", unit="N*m")
        self.add_inward("a", 0.0, desc="Acceleration", unit="m/s**2")

        # Outputs
        self.add_outward("alpha", 0.0, desc="Angular acceleration", unit="1/s**2")
        self.add_outward("omega", 0.0, desc="Angular velocity", unit="1/s")
        self.add_outward("weight", 0.0, desc="Weight", unit="kg")
        self.add_outward("force", 0.0, desc="Force", unit="N")

        # Transients
        self.add_transient("w", der="alpha", desc="Angular velocity")

    def compute(self):

        self.alpha = self.a / self.R
        self.force = (self.M - 2 * self.mw * self.R**2 * self.alpha) / self.R
        self.omega = self.w
        self.weight = 4 * self.mw
