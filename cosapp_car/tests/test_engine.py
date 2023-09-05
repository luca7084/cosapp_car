import numpy as np

from cosapp_car.systems import Engine

class TestEngine:

    def test_run_once(self):

        sys = Engine('sys')
        sys.w_in = 2.

        sys.run_once()

        np.testing.assert_allclose(sys.M, 20., atol=10**(-4))