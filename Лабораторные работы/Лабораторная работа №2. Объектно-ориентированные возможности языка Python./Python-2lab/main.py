from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np  # пример внешнего пакета

def main():
    N = 5  # номер варианта
    
    # Создаем объекты
    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")
    
    # Выводим информацию о фигурах
    print(rectangle)
    print(circle)
    print(square)
    
    # Пример использования внешнего пакета
    arr = np.array([1, 2, 3])
    print("\nПример работы с внешним пакетом (numpy):")
    print("Сумма элементов массива:", np.sum(arr))

if __name__ == "__main__":
    main()
