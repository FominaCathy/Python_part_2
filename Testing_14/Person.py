class ValidLevel:
    def __init__(self, level):
        self.level = level

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value):
        # оставила чтобы падал.
        if value > instance._MAX_LEVEL or value < instance._MIN_LEVEL:
            raise ValueError(
                f"уровень доступа должен быть в диапазоне от {instance._MIN_LEVEL} до {instance._MAX_LEVEL}")
        instance.__dict__[self.param_name] = value


class Person:
    _MIN_LEVEL = 1
    _MAX_LEVEL = 8
    level = ValidLevel('_level')

    def __init__(self, name, num_id, level):

        self.level = level
        self.name = name
        self.num_id = num_id

    def __str__(self):
        return f'name: {self.name}, id: {self.num_id}, level: {self.level}'

    def __eq__(self, other):
        return self.num_id == other.num_id and self.name == other.name

    def __hash__(self):
        return hash((self.num_id, self.name))



