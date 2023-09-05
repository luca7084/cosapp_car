from cosapp.base import System


class Engine(System):
    def setup(self):

        # Engine parameters
        self.add_inward("K", 10.0, desc="Constant", unit="m**2/s")

        # Inputs
        self.add_inward("w_in", 0.0, desc="Fuel income flux", unit="kg/s")

        # Outputs
        self.add_outward("M", 0.0, desc="Produced torque", unit="N*m")
        self.add_outward("weight", 2.0, desc="Engine weight", unit="kg")

    def compute(self):

        self.M = self.K * self.w_in
