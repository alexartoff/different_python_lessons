# TASK
# Реализуйте класс HourClock, который будет изображать часы с одной лишь часовой стрелкой.
# Текущее время (час) должно сообщать свойство hours. Это же свойство должно позволять изменять
# положение часовой стрелки (посредством сеттера). При изменении положения стрелки нужно контролировать,
# чтобы значение оставалось в диапазоне 0..11 (часов).


class HourClock:
    def __init__(self):
        self.time = 0

    @property
    def hours(self):
        return self.time % 12

    @hours.setter
    def hours(self, new):
        self.time = new
    

clock = HourClock()
clock.hours  # 0
# в начале часовая стрелка всегда на нуле
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 6
clock.hours  # 11
clock.hours += 4
clock.hours  # 3
clock.hours -= 4
clock.hours  # 11
clock.hours = 123
clock.hours  # 3
