import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled = True):
        self.__sides = sides   # (список сторон(целые числа))
        self.__color = list(color)   # (список цветов в формате RGB)
        self.filled = filled   # (закрашенный, bool)

    def get_color(self):   # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b): # проверяет корректность значений перед установкой нового цвета
        return r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255

    def set_color(self, r, g, b):    # изменяет цвет
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, args):     #возвращает True если все стороны целые положительные числа
        return len(args) == len(self.__sides) and min(args) > 0   # и кол-во новых сторон совпадает с текущим

    def get_sides(self):
        return self.__sides

    def __len__(self):      # периметр фигуры
        count = 0
        for i in self.__sides:
            count += i
        return count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) == 1 and sides[0] > 0:
            super().__init__(color, list(sides))
        else:
            super().__init__(color, [1])
        self.__radius = super().__len__() / (2 * math.pi)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = super().__len__() / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == 3 and min(sides) > 0:
            super().__init__(color, list(sides))
        else:
            super().__init__(color, [1 for i in range(1, self.sides_count + 1)])
        p = super().__len__() / 2
        self.__height = 2 / self._Figure__sides[0] * math.sqrt(p * (p - self._Figure__sides[0])
                                    * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        p = super().__len__() / 2
        self.__height = 2 / self._Figure__sides[0] * math.sqrt(p * (p - self._Figure__sides[0])
                                    * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))

    def get_square(self):
        return 0.5 * self.__height * self._Figure__sides[0]

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1 and sides[0] > 0:
            super().__init__(color, [sides[0] for i in range(1,self.sides_count+1)])
        else:
            super().__init__(color, [1 for i in range(1,self.sides_count+1)])

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((2, 33, 70), 4)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print('Цвета круга:', circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print('Цвета куба:', cube1.get_color())
triangle1.set_color(300, 70, 15) # Не изменится
print('Цвета треугольника:', triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print('Размеры куба:', cube1.get_sides())
circle1.set_sides(15) # Изменится
print('Размеры круга:', circle1.get_sides())
triangle1.set_sides(2, 2, 2) # Изменится
print('Размеры треугольника:', triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print('Длина круга:', len(circle1))
print('Площадь круга:', circle1.get_square())

# Проверка объёма (куба):
print('Объем куба:', cube1.get_volume())

# Проверка площади (треугольника):
print('Площадь треугольника:', triangle1.get_square())
