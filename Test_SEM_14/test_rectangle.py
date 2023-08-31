"""
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
   а также вычисляющую периметр, площадь и позволяющий складывать и вычитать
   прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.
"""
from Rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect_first = Rectangle(1, 5)
        self.rect_second = Rectangle(2, 2)


    def test_area(self):
        self.assertEqual(Rectangle(5, 2).area, 10)

    def test_perimetr(self):
        self.assertEqual(Rectangle(5, 2).perimetr, 14)

    def test_negativ_value(self):
        self.assertRaises(ValueError, Rectangle, -2, 5)

    def test_sub_rect(self):
        self.assertTrue((Rectangle(1, 5) - Rectangle(2, 2)) == Rectangle(1, 3))

    def test_add_rect(self):
        self.assertEqual((Rectangle(1, 5) + Rectangle(2, 2)), Rectangle(3, 7))


if __name__ == '__main__':
    unittest.main(verbosity=2)
