import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestFigures(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(5, 10, "красного")
        self.assertEqual(rect.area(), 50)
        self.assertEqual(rect.get_name(), "Прямоугольник")

    def test_circle(self):
        circ = Circle(5, "синего")
        self.assertAlmostEqual(circ.area(), 78.539816, places=4)
        self.assertEqual(circ.get_name(), "Круг")

    def test_square(self):
        sq = Square(5, "зеленого")
        self.assertEqual(sq.area(), 25)
        self.assertEqual(sq.get_name(), "Квадрат")


if __name__ == "__main__":
    unittest.main()
