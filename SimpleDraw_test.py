import simple_draw as sd
print('Введите номер желаемого цвета')
c = int(input())

colors = {0: 'red', 1: 'orange', 2: 'yellow', 3: 'green',
                  4: 'cyan', 5: 'blue', 6: 'purple'}
sd.resolution = (1200, 800)
sd.background_color = 'white'
p1 = sd.get_point(100,100)
p2 = sd.get_point(300,300)
sd.rectangle(p1,p2,color=colors[c])
sd.pause()