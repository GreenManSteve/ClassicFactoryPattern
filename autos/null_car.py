from autos.abs_auto import AbsAuto


class NullCar(AbsAuto):
    def start(self):
        print("{} detected".format(self.name))

    def stop(self):
        pass
