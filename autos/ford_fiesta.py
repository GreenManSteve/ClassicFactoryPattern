from autos.abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    def start(self):
        print("Starting {}".format(self.name))

    def stop(self):
        print("Stopping {}".format(self.name))