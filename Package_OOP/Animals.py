"""
задание 5
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

задание 6
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки

Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Animals:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f'{self.name}'


class Fish(Animals):
    def __init__(self, name, depth: int):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'{self.name},  глубина обитания (м): {self.depth}'


class Dog(Animals):
    def __init__(self, name, breed: str):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'{self.name}, порода: {self.breed}'


class Snake(Animals):
    def __init__(self, name, toxicity: bool):
        super().__init__(name)
        self.toxicity = toxicity

    def get_info(self):
        return f'{self.name}, ядовитость: {"Yes" if self.toxicity else "No"}'


class Cat(Animals):
    def __init__(self, name, long_haired: bool):
        super().__init__(name)
        self.long_haired = long_haired

    def get_info(self):
        return f'{self.name}, длиношерстность: {"Yes" if self.long_haired else "No"}'


class AnimalsFactory:
    def __init__(self):
        self.dict_type_str = {str(item.__name__): item for item in Animals.__subclasses__()}
        self.list_type_cls = Animals.__subclasses__()

    def create_animal(self, type_animal, *args):
        if type(type_animal) == str:

            if self.dict_type_str.get(type_animal) is None:
                raise ValueError('такого вида животного нет')

            return self.dict_type_str[type_animal](*args)
        else:
            if type_animal in self.list_type_cls:
                return type_animal(*args)
            else:
                raise ValueError('нe входит в класс животных')


if __name__ == '__main__':
    fabric = AnimalsFactory()
    som = fabric.create_animal('Fish', 'Som', 15)
    tosha = fabric.create_animal(Dog, 'Tosha', 'beagle')
    zoya = fabric.create_animal(Snake, 'Zoya', True)
    bagel = fabric.create_animal('Cat', 'bagel', True)

    print(som.get_info())
    print(tosha.get_info())
    print(f'{zoya.get_info() = }')
    print(f'{bagel.get_info() = }')
