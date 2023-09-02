'''
Задача 6
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.

'''
import pytest

from Project import Project

from Person import Person


@pytest.fixture
def project():
    test_project = Project(4)
    test_project.load_data('test_bd.json')
    return test_project


def test_authorize_valid(project, capfd):
    project.authorize("ivan", "8p")
    captured = capfd.readouterr()
    assert captured.out == 'ivan, Добро пожаловать в проект\n'


def test_authorize_non_valid(project, capfd):
    project.authorize("macyanya", "lala")
    captured = capfd.readouterr()
    assert captured.out == 'пользователь "macyanya, id: lala" не может зайти в проект: нет списке группы проекта\n'


def test_authorize_non_access(project, capfd):
    project.authorize("willy", "9e")
    captured = capfd.readouterr()
    assert captured.out == 'пользователь willy не может зайти в проект: низкий уровень доступа (3)\n'


def test_add_user_valid(project, capfd):
    project.add_user(Person('mumu', 'mu', 6))
    captured = capfd.readouterr()
    assert captured.out == 'пользователь name: mumu, id: mu, level: 6 добавлен в проект\n'


def test_add_lower_access(project, capfd):
    project.add_user(Person('goblin', '456', 2))
    captured = capfd.readouterr()
    assert captured.out == 'пользователь goblin не может добавлен в проект: низкий уровень доступа (2)\n'


if __name__ == "__main__":
    pytest.main(['-v'])
