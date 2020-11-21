import simple_draw as sd
sd.resolution = (1200, 800)
point_1 = sd.get_point(600,0)
point = sd.get_point(600, 300)
angle = 90
lenght = 100
def branch(point, angle, length):
     if length >10:
        v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=3)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=3)
        v2.draw()
        branch(v1.end_point,angle+30,length*0.8)
        branch(v2.end_point, angle-30, length * 0.8)
sd.line(point_1,point,width=5)
branch(point=point, angle=angle, length=lenght)

sd.pause()
