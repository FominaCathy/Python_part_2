import Person

class ExceptionProject(Exception):
    pass


class AccessError(ExceptionProject):
    def __init__(self, user: Person):
        self.user = user

    def __str__(self):
        return f'пользователь "{self.user.name}, id: {self.user.num_id}" не может зайти в проект: нет списке группы проекта'


class LevelError(ExceptionProject):
    def __init__(self, user: Person, actor: str):
        self.actor = actor
        self.user = user

    def __str__(self):
        return f"пользователь {self.user.name} не может {self.actor}: низкий уровень доступа ({self.user.level})"