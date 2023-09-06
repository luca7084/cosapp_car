import numpy as np

from cosapp_car.systems import Brakes


class TestAcel:
    def test_run_once(self):

        sys = Brakes("sys")
        sys.press = True

        sys.run_once()

        np.testing.assert_allclose(sys.lock, True, atol=10 ** (-4))
