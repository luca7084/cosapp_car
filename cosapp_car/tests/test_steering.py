import numpy as np

from cosapp_car.systems import Car, SteeringWheel


class TestSteering:
    def test_run_once(self):

        sys = SteeringWheel("sys")
        sys.run_once()

    def test_transmission(self):

        sys = Car("sys")
        sys.ster.angle = 20.0
        sys.ster.factor = 10.0
        sys.run_once()

        np.testing.assert_allclose(sys.wheels.phi, 2.0, atol=10 ** (-4))
