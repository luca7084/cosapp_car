from cosapp_car.systems import Accelerator
import numpy as np

class TestAcel:

    def test_run_once(self):

        sys = Accelerator('sys')
        sys.delta = 0.4
        
        sys.run_once()

        np.testing.assert_allclose(sys.w_command, 0.4, atol=10**(-4))