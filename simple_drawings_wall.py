import simple_draw as sd

def brick(x,y):
    point1 = sd.get_point(x, y)
    point2 = sd.get_point(x + brick_lengh, y + brick_height)
    sd.rectangle(point1, point2, 'white', int(brick_lengh/20))

brick_lengh=20
brick_height=int(brick_lengh/2)
limit=1000

sd.resolution = (limit, limit)
sd.background_color = 'red'
for y in range(0, limit+brick_height, brick_height):
    for x in range(0,limit+brick_lengh,brick_lengh):
        if y%(2*brick_height) != 0:
            x-=brick_lengh/2
        brick(x,y)
sd.pause()
sd.rec