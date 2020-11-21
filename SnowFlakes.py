import simple_draw as sd

sd.resolution = (1200,800)

xlist, ylist = [], []

for _ in range(50):
    xlist.append(sd.randint(100,1100))
    ylist.append(sd.randint(500,800))

def snowflake(x, y):
    a = 1
    while True:
        sd.clear_screen()
        for i in range(len(x)):
            point = sd.get_point(x[i],y[i])
            sd.snowflake(center=point, length=50, color='white')
            h = sd.randint(0, 20)
            y[i] -= h
            if y[i] < 50:
                break
            a = sd.randint(-1,1)

            x[i] = x[i] + h*a
        sd.sleep(0.05)
        if sd.user_want_exit():
            break
snowflake(xlist,ylist)

sd.pause()
