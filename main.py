
"""Учебный рисунок: ступенчатая линия и сетка точек с Python Turtle."""

import turtle as t

# Параметры рисунка
SCALE = 9
COLOR = "purple"
STEPS = 4

DOT_COLUMNS = 30
DOT_Y_START = -10
DOT_Y_STOP = 15  # Верхняя граница не включается
DOT_SIZE = 3

# Размеры графической области
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 500


def calculate_offsets():
    """Вычислить смещение для центрирования рисунка."""

    # Границы сетки точек
    grid_min_x = 0
    grid_max_x = (DOT_COLUMNS - 1) * SCALE

    grid_min_y = DOT_Y_START * SCALE
    grid_max_y = (DOT_Y_STOP - 1) * SCALE

    # Центрирование относительно начала координат Turtle
    offset_x = -(grid_min_x + grid_max_x) / 2
    offset_y = -(grid_min_y + grid_max_y) / 2

    return offset_x, offset_y


def draw_steps(offset_x, offset_y):
    """Нарисовать ступенчатую линию."""

    t.penup()
    t.goto(offset_x, offset_y)
    t.setheading(90)
    t.color(COLOR)
    t.pensize(2)
    t.pendown()

    for _ in range(STEPS):
        t.forward(7 * SCALE)
        t.right(90)

        t.forward(7 * SCALE)
        t.left(90)

        t.forward(7 * SCALE)
        t.right(90)


def draw_dot_grid(offset_x, offset_y):
    """Разместить точки в прямоугольной сетке."""

    t.penup()
    t.color(COLOR)

    for x in range(DOT_COLUMNS):
        for y in range(DOT_Y_START, DOT_Y_STOP):
            t.goto(
                offset_x + x * SCALE,
                offset_y + y * SCALE
            )
            t.dot(DOT_SIZE)


def main():
    """Запустить приложение Turtle."""

    screen = t.Screen()
    screen.title("Python Turtle — ступени и сетка точек")

    # Размеры окна
    screen.setup(
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT
    )

    screen.bgcolor("white")

    # Явная система координат, соответствующая размерам окна
    screen.setworldcoordinates(
        -WINDOW_WIDTH / 2,
        -WINDOW_HEIGHT / 2,
        WINDOW_WIDTH / 2,
        WINDOW_HEIGHT / 2
    )

    # Отключаем анимацию для быстрой отрисовки
    screen.tracer(0)

    t.speed(0)
    t.hideturtle()

    # Рассчитываем положение рисунка
    offset_x, offset_y = calculate_offsets()

    # Рисуем
    draw_steps(offset_x, offset_y)
    draw_dot_grid(offset_x, offset_y)

    # Обновляем экран
    screen.update()

    # Закрываем окно по щелчку мыши
    screen.exitonclick()


if __name__ == "__main__":
    main()
