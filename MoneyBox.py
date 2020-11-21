class MoneyBox:
    def __init__(self, capacity=100):
        self.coin_count = 0
        self.capacity = capacity
    def can_add(self, v):
        return self.coin_count + v <= self.capacity
    def add(self,v):
        if self.can_add(v):
            self.coin_count+=v

a=MoneyBox()
print(a.capacity)
a.add(1)
print(a.coin_count)


