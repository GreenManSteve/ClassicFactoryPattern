from autos.chevy_volt import ChevyVolt
from factories.abs_factory import AbsFactory


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = "ChevyVolt"
        return chevy