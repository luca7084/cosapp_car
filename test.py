from cosapp.drivers import NonLinearSolver, RungeKutta
from cosapp.recorders import DataFrameRecorder

from cosapp_car.systems import Car

car = Car("car")
car.tank.w_out_max = 1.0

car.add_driver(NonLinearSolver("solver"))
car.run_drivers()

print(car.dyn.a)
print(car.wheels.alpha)
print(car.wheels.F)
print(car.dyn.weight)

car = Car("car")
car.tank.w_out_max = 1.0
car.tank.weight_p = 5.0

driver = car.add_driver(RungeKutta(order=4, dt=1.0))
solver = driver.add_child(NonLinearSolver("solver", tol=10 ** (-5)))
driver.time_interval = (0, 5)
driver.add_recorder(DataFrameRecorder(includes=["dyn.a", "wheels.alpha", "wheels.F", "dyn.weight"]))

car.run_drivers()
data = driver.recorder.export_data()
print(data)
