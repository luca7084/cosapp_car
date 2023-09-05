import numpy as np
from cosapp.drivers import RungeKutta

from cosapp_car.systems import Tank


class TestTank:
    def test_run_once(self):

        sys = Tank("sys")

        sys.run_once()

    def test_fuel(self):

        sys = Tank("sys")

        sys.w_out_max = 0.0
        sys.w_in = 2.0
        sys.weight_p = 0.0

        driver = sys.add_driver(RungeKutta(order=4, dt=1.0))
        driver.time_interval = (0, 5)

        sys.run_drivers()

        np.testing.assert_allclose(sys.weight_prop, 10.0, atol=10 ** (-4))

    def test_burn(self):

        sys = Tank("sys")

        sys.w_out_max = 3.0
        sys.weight_p = 30.0

        driver = sys.add_driver(RungeKutta(order=4, dt=1.0))
        driver.time_interval = (0, 5)

        sys.run_drivers()

        np.testing.assert_allclose(sys.weight_prop, 15.0, atol=10 ** (-4))
