from autos.ford_fiesta import FordFiesta
from factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordFiesta()
        ford.name = "FordFiesta"
        return ford