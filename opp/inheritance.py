# TASK
# Вам дан класс Counter, реализующий счётчик с инкрементом и декрементом.
# Вам нужно реализовать класс-потомок LimitedCounter, который будет отличаться от Counter тем,
# что при инициализации будет принимать в качестве аргумента лимит — максимальное возможное значение счётчика.
# Требования к классу LimitedCounter:
# * Класс должен максимально использовать методы предка, если таковые переопределяет.
# * Минимальное значение счётчика Counter — 0, должно оставаться таковым и для LimitedCounter.


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# Решение основано на замене атрибута value на свойство,
# setter которого ограничивает значение счётчика.
# Такой подход позволяет сохранить свойства класса даже
# если пользователь будет менять значение счётчика через
# присваивание напрямую атрибуту value.
class LimitedCounter(Counter):
    def __init__(self, limit):
        self.limit = limit
        # Инициализация методом родителя делается в конце,
        # потому что предок уже в __init__ присваивает атрибуту
        # value значение 0. А это значит, что будет вызван setter,
        # который использует атрибуты limit и current_value.
        super().__init__()
    
    @property
    def value(self):
        return self.current_value
    
    @value.setter
    def value(self, new):
        if new > self.limit:
            self.current_value = self.limit
        else:
            self.current_value = new


counter = LimitedCounter(limit=10)
counter.inc()
counter.inc(7)
counter.value  # 8
counter.dec(10)
counter.value  # 0
counter.inc(7)
counter.inc(7)
counter.value  # 10
