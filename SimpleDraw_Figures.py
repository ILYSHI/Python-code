import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
sd.resolution = (1200, 600)
length = 100
angle = 0
point = sd.get_point(500, 200)

shapes_dict = {0: 'треугольник', 1: 'квадрат', 2: 'пятиугольник', 3: 'шестиугольник'}
# определим предложенные фигуры
print('Возможные фигуры:')
for k, v in shapes_dict.items():
    print(k, ':', v)  # выведем фигуры на консоль


def triangle(point, angle, length):  # функция для треугольника
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


def square(point, angle, length):  # функция для квадрата
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()


def pentagon(point, angle, length):  # функция для пятиугольника
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw()


def nexagon(point, angle, length):  # функция для шестиугольника
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw()


def shapes_input():  # функция для ввода числа желаемой фигуры
    print('Введите желаемую фигуру:')
    shapes_number = int(input())
    if shapes_number == 0:
        triangle(point=point, angle=angle, length=200)
    elif shapes_number == 1:
        square(point=point, angle=angle, length=200)
    elif shapes_number == 2:
        pentagon(point=point, angle=angle, length=200)
    elif shapes_number == 3:
        nexagon(point=point, angle=angle, length=200)
    else:  # отсекаем некорректные значения чисел введеных пользователем
        print('Вы ввели некорректный номер!')
        return shapes_input()

while True:
    shapes_input()  # функция со значением числа, введенным пользователем

sd.pause()