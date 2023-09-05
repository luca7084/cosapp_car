from cosapp.base import System

from cosapp_car.systems import Dynamics, Engine, Tank, Wheels


class Car(System):
    """A simple model of a car.

    Inputs
    ------

    Outputs
    ------
    a [m/s**2]: float,
        car acceleration

    """

    def setup(self):

        self.add_child(Tank("tank"))
        self.add_child(Engine("engine"))
        self.add_child(Wheels("wheels"))
        self.add_child(
            Dynamics(
                "dyn",
                forces=["friction"],
                weights=["weight_wheels", "weight_engine", "weight_tank"],
            ),
            pulling=["a"],
        )

        self.connect(self.tank.outwards, self.engine.inwards, {"w_out": "w_in"})
        self.connect(self.engine.outwards, self.wheels.inwards, ["M"])

        self.connect(
            self.wheels.outwards, self.dyn.inwards, {"weight": "weight_wheels", "force": "friction"}
        )
        self.connect(self.tank.outwards, self.dyn.inwards, {"weight_prop": "weight_tank"})
        self.connect(self.engine.outwards, self.dyn.inwards, {"weight": "weight_engine"})

        self.connect(self.dyn.outwards, self.wheels.inwards, ["a"])
