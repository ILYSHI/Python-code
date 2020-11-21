# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
res_x = 1200
res_y = 600
sd.resolution = (res_x, res_y)
length = 200
angle = 0
center_point = sd.get_point(res_x/2,res_y/2)

# TODO у меня в словаре названия служат для визуализации выбора


# TODO функции объявляем до основной логики программы!
# TODO используем обновленный код от 01 задания
def triangle():
    for angle in range(0, 361, 120):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point


def square():
    v0 = sd.get_vector(start_point=center_point,angle=225,length = length/2*(2)**(1/2))
    point = v0.end_point
    for angle in range(0, 361, 90):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point


def pentagon():
    v0 = sd.get_vector(start_point=center_point,angle=180+(108/2),length = length*0.85)
    point = v0.end_point
    for angle in range(0, 361, 72):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point


def nexagon():
    v0 = sd.get_vector(start_point=center_point, angle=240, length=length)
    point = v0.end_point

    for angle in range(0, 361, 60):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point


shapes = {'0': 'треугольник', '1': 'квадрат', '2': 'пятиугольник', '3': 'шестиугольник'}

# определим предложенные фигуры
print('Возможные фигуры:')
# TODO Корректировки от 02 задания
for key, shapes_value in shapes.items():
    print(key, ':', shapes_value)  # выведем фигуры на консоль


while True:
    print('Введите желаемую фигуру:')
    shapes_number = input()

    if shapes_number not in shapes:
        print('Вы ввели некорректный номер!')
        continue
    if shapes_number == '0':
        triangle()
    elif shapes_number == '1':
        square()
    elif shapes_number == '2':
        pentagon()
    elif shapes_number == '3':
        nexagon()
    break


sd.pause()