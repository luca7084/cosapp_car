import numpy as np
from cosapp.drivers import NonLinearSolver

from cosapp_car.systems import Wheels


class TestWheels:
    def test_run_once(self):

        sys = Wheels("sys")

        sys.run_once()

    def test_NLS(self):

        sys = Wheels("sys")
        sys.a = 4.0
        sys.M = 32.0

        sys.add_driver(NonLinearSolver("solver", tol=10 ** (-6)))
        sys.run_drivers()

        np.testing.assert_allclose(sys.F, 2.0, atol=10 ** (-4))
