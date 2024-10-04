from factories import loader

for factory_name in "chevy_factory", "ford_factory", "bmw_factory":
    factory = loader.load_factory(factory_name)
    car = factory.create_auto()
    car.start()
    car.stop()
