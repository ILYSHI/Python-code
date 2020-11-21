import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime())+": " + str(msg))
class LoggableList(list,Loggable):
    def append(self,b):
        self.log(b)
        return super(LoggableList,self).append(b)



z = LoggableList()
z.append('Hello!')
z.append('Good bye')
print(z)