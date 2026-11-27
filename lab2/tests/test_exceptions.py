from src import exceptions

def test_all_exceptions_inherit_from_plant_exception():
    for name in dir(exceptions):
        if name.endswith("Exception") and name != "PlantException":
            cls = getattr(exceptions, name)
            assert issubclass(cls, exceptions.PlantException)