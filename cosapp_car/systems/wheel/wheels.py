from cosapp.base import System
from cosapp.multimode import Event
import numpy as np

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

        # Parameters
        self.add_inward("R", 2.0, desc="Wheel radius", unit="m")
        self.add_inward("mw", 1.0, desc="Wheel mass", unit="kg")
        self.add_inward("mu", 0.2, desc="Wheels friction coefficient", unit="")
        self.add_outward("moving", True, desc="Whether the wheels are moving or not")

        # inputs
        self.add_inward("M", 0.0, desc="External torque", unit="N*m")
        self.add_inward("a", 0.0, desc="Acceleration", unit="m/s**2")
        self.add_inward("lock", False, desc="Whether the wheels are locked or not")
        self.add_inward("normal", 0.0, desc="Normal force", unit="N")
        self.add_inward("v", 0., desc="Velocity", unit='m/s')

        # Outputs
        self.add_outward("alpha", 0.0, desc="Angular acceleration", unit="1/s**2")
        self.add_outward("omega", 0.0, desc="Angular velocity", unit="1/s")
        self.add_outward("weight", 4 * self.mw, desc="Weight", unit="kg")
        self.add_outward("force", 0.0, desc="Force", unit="N")

        # Transients
        self.add_transient("w", der="alpha", desc="Angular velocity")

        # Events
        self.add_event("forward", trigger="v > 0.")
        self.add_event("backwards", trigger="v < 0.")
        self.add_event("start", trigger=Event.merge(self.forward, self.backwards))
        self.add_event("stop", trigger="v == 0.")

    def compute(self):

        self.alpha = (self.a / self.R) * (1 - self.lock)

        rot_fric = (self.M - 2 * self.mw * self.R**2 * self.alpha) / self.R
        slid_fric = - self.mu * self.normal * self.moving
        self.force = rot_fric * (1 - self.lock) + slid_fric * self.lock

        self.omega = self.w
        self.w *= (1 - self.lock)

    def transition(self):

        if self.start.present:
            self.moving = True
        if self.stop.present:
            self.moving = False
