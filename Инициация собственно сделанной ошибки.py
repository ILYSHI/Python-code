class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(sel,x):
        if x>0:
            return super().append(x)
        else: raise NonPositiveError
d=PositiveList()
d.append(2)
print(d)
d.append(-1)