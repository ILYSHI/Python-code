class Buffer:
    def __init__(self):
        self.buf = []
    def add(self,*a):
        for i in a:
            self.buf.append(i)
        while len(self.buf)>=5:
            print(sum(self.buf[:5]))
            self.buf=self.buf[5:]
    def get_current_part(self):
        return self.buf

buf=Buffer()
buf.add(1,2,3)
print(buf.get_current_part())
buf.add(4,5,6)
print(buf.get_current_part())
buf.add(7,8,9,10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())
