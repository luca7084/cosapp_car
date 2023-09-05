from cosapp.base import System


class Wheels(System):
    def setup(self):

        # Geometric parameters
        self.add_inward("R", 2.0, desc="Wheel radius", unit="m")
        self.add_inward("mw", 1.0, desc="Wheel mass", unit="kg")

        # inputs
        self.add_inward("M", 0.0, desc="External torque", unit="N*m")
        self.add_inward("F", 0.0, desc="Friction force", unit="N")
        self.add_inward("a", 0.0, desc="Acceleration", unit="m/s**2")
        self.add_inward("alpha", 0.0, desc="Angular acceleration", unit="1/s**2")

        # Outputs
        self.add_outward("omega", 0.0, desc="Angular velocity", unit="1/s")
        self.add_outward("weight", 0.0, desc="Weight", unit="kg")
        self.add_outward("force", 0.0, desc="Force", unit="N")

        # Transients
        self.add_transient("w", der="alpha", desc="Angular velocity")

        # Mathematical problem
        self.add_unknown("F")
        self.add_unknown("alpha")
        self.add_equation("M - 4*F*R == 2*mw*R**2*alpha")
        self.add_equation("a == alpha*R")

    def compute(self):

        self.omega = self.w
        self.weight = 4 * self.mw
        self.force = 4 * self.F
