import numpy as np

from cosapp_car.systems.physics import Dynamics


class TestDynamics:
    def test_run_once(self):

        sys = Dynamics("dyn", forces=["F1", "F2"], weights=["w1", "w2"])

        sys.F1 = 5.0
        sys.F2 = 4.0
        sys.w1 = 2.0
        sys.w2 = 1.0

        sys.run_once()

        np.testing.assert_allclose(sys.a, 3.0, atol=10 ** (-4))
        np.testing.assert_allclose(sys.weight, 3.0, atol=10 ** (-4))
