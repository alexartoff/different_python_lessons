# TASK
# Реализуйте класс Counter, представляющий собой счётчик, хранящий неотрицательное целочисленное значение и позволяющий это значение изменять:
# атрибут value должен хранить текущее значение счётчика (вначале равное нулю),
# метод inc(delta=1) должен увеличивать текущее значение на delta единиц (на 1 по умолчанию),
# метод dec(delta=1) должен уменьшать текущее значение на delta единиц.

class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta
        return self.value

    def dec(self, delta=1):
        self.value -= delta
        if self.value < 0:
            self.value = 0
        return self.value


c = Counter()
c.inc()
c.inc()
c.inc(40)
c.value  # 42
c.dec()
c.dec(30)
c.value  # 11
c.dec(delta=100)
c.value  # 0


# TASK
# Вам предстоит снова реализовать класс Counter.
# Но на этот раз счётчик будет иммутабельный (и всё ещё неотрицательный целочисленный):
# методы inc и dec должны возвращать новый счётчик с изменённым значением.
# Атрибут value всё ещё должен содержать текущее значение. В этой реализации вам нужно объявить в классе инициализатор,
# позволяющий задать начальное значение счётчика (атрибут value). Если же значение при инстанциировании не будет задано,
# следует принять его равным нулю. Внимание, в самом классе атрибут value не должен быть объявлен.
# Этот атрибут должен добавляться в объект в инициализаторе. Методы inc(delta=1) и dec(delta=1) должны возвращать
# новый экземпляр счётчика. Старый же экземпляр не должен изменяться при этом!

class Counter:
    def __init__(self, value=0):
        self.value = value

    def inc(self, delta=1):
        val = self.value + delta
        return Counter(val)

    def dec(self, delta=1):
        val = self.value - delta
        if val < 0:
            val = 0
        return Counter(val)


c = Counter()
c.inc().inc(5).dec(2).value  # 4
d = c.inc(100)
d.dec().value  # 99
forty_two = Counter(42)
forty_two.value  # 42
