from cosapp.base import System


class Tank(System):
    """A simple model of a fuel tank.

    Inputs
    ------
    w_in [kg/s]: float,
        mass flow of fuel entering the tank

    Outputs
    ------
    w_out [kg/s]: float,
        mass flow of fuel exiting the tank
    weight_prop [kg]: float,
        fuel weight
    """

    def setup(self):

        # Flux control
        self.add_inward("w_out_max", 0.0, desc="Fuel output rate", unit="kg/s")

        # Inputs
        self.add_inward("w_in", 0.0, desc="Fuel income rate", unit="kg/s")

        # Outputs
        self.add_outward("w_out", 0.0, desc="Fuel output rate", unit="kg/s")
        self.add_outward("weight_prop", 0.0, desc="Proppellant weight", unit="kg")

        # Transient
        self.add_transient("weight_p", der="w_in - w_out", desc="Propellant weight")

    def compute(self):

        self.w_out = self.w_out_max
        self.weight_prop = self.weight_p
