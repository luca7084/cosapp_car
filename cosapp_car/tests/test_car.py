import numpy as np
from cosapp.drivers import NonLinearSolver, RungeKutta

from cosapp_car.systems import Car


class TestCar:
    def test_run_once(self):

        sys = Car("sys")
        sys.run_once()

    def test_NLS(self):

        sys = Car("sys")

        sys.tank.w_out_max = 1.0
        sys.acel.delta = 1.0

        sys.add_driver(NonLinearSolver("solver", tol=10 ** (-6)))
        sys.run_drivers()

        np.testing.assert_allclose(sys.dyn.a, 5 / 8, atol=10 ** (-4))
        np.testing.assert_allclose(sys.dyn.weight, 6.0, atol=10 ** (-4))
        np.testing.assert_allclose(sys.wheels.alpha, 5 / 16, atol=10 ** (-4))
        np.testing.assert_allclose(sys.wheels.force, 15 / 4, atol=10 ** (-4))

    def test_rk(self):

        sys = Car("sys")

        sys.tank.w_out_max = 1.0
        sys.tank.weight_p = 5.0
        sys.acel.delta = 1.0

        driver = sys.add_driver(RungeKutta(order=4, dt=1.0))
        solver = driver.add_child(NonLinearSolver("solver", tol=10 ** (-5)))
        driver.time_interval = (0, 5)

        sys.run_drivers()

        np.testing.assert_allclose(sys.dyn.a, 5 / 8, atol=10 ** (-4))
        np.testing.assert_allclose(sys.dyn.weight, 6.0, atol=10 ** (-4))
        np.testing.assert_allclose(sys.wheels.alpha, 5 / 16, atol=10 ** (-4))
        np.testing.assert_allclose(sys.wheels.force, 15 / 4, atol=10 ** (-4))
