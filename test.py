from cosapp_car.systems import Car
from cosapp.drivers import NonLinearSolver, RungeKutta
from cosapp.recorders import DataFrameRecorder

car = Car("car")
car.tank.w_out_max = 1.

car.add_driver(NonLinearSolver('solver'))
car.run_drivers()

print(car.dyn.a)
print(car.wheels.alpha)
print(car.wheels.F)
print(car.dyn.weight)


