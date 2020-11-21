import simple_draw as sd

sd.resolution = (1200, 600)
point_0 = sd.get_point(600, 5)
angle = 90
length = 100


def drow_branches(point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle + 30
    next_length = length * .75
    v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v2.draw()
    next_point1 = v2.end_point
    next_angle1 = angle + 30
    next_length1 = length * .75
    drow_branches(point=next_point1, angle=next_angle1, length=next_length1)
drow_branches(point_0, angle, length)
sd.pause()