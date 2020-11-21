import simple_draw as sd

def draw_branches(start_point,angle,lenght,width):
    lenght *=0.8
    if width >1:
        width-=1
    if lenght > 10:
        sd.vector(start_point,angle-30,lenght,color='black',width=width)
        sd.vector(start_point, angle + 30, lenght,color='black',width=width)
        new_point_1 = sd.get_point(start_point.x+sd.cos(angle-30)*lenght,start_point.y+sd.sin(angle-30)*lenght)
        new_point_2 = sd.get_point(start_point.x + sd.cos(angle + 30) * lenght, start_point.y + sd.sin(angle + 30) * lenght)
        draw_branches(new_point_1,angle-sd.randint(15,45),lenght*sd.randint(90,110)/100,width)
        draw_branches(new_point_2,angle+sd.randint(15,45),lenght*sd.randint(90,110)/100,width)
    else:
        new_point_1 = sd.get_point(start_point.x + sd.cos(angle - 30) * lenght, start_point.y + sd.sin(angle - 30) * lenght)
        new_point_2 = sd.get_point(start_point.x + sd.cos(angle + 30) * lenght, start_point.y + sd.sin(angle + 30) * lenght)
        color = (sd.randint(0,100),sd.randint(140,250), sd.randint(10,40))
        sd.circle(new_point_1,5,color=color,width=0)
        sd.circle(new_point_2, 5, color=color,width=0)

limit=1000

sd.resolution = (1200, 800)
sd.background_color = 'white'
middle = sd.get_point(600,0)
root_point = sd.get_point(600,200)
sd.line(middle,root_point,color='black',width=15)
test = sd.get_vector(root_point,30,200)

draw_branches(root_point,90,100/0.8,10)

sd.pause()
sd.take_snapshot('Tree.png')