from autos.null_car import NullCar
from factories.abs_factory import AbsFactory


class NullFactory(AbsFactory):
    def create_auto(self):
        self.nocar = nocar = NullCar()
        nocar.name = "NullCar"
        return nocar