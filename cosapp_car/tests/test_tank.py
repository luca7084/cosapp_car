import numpy as np

from cosapp_car.systems import Tank
from cosapp.drivers import RungeKutta

class TestTank:

    def test_run_once(self):

        sys = Tank('sys')

        sys.run_once()

    def test_fuel(self):

        sys = Tank('sys')

        sys.w_out_max = 0.
        sys.w_in = 2.
        sys.weight_p = 0.

        driver = sys.add_driver(RungeKutta(order=4, dt = 1.))
        driver.time_interval = (0, 5)

        sys.run_drivers()

        np.testing.assert_allclose(sys.weight_prop, 10., atol=10**(-4))

    def test_burn(self):

        sys = Tank('sys')

        sys.w_out_max = 3.
        sys.weight_p = 30.

        driver = sys.add_driver(RungeKutta(order=4, dt = 1.))
        driver.time_interval = (0, 5)

        sys.run_drivers()

        np.testing.assert_allclose(sys.weight_prop, 15., atol=10**(-4))