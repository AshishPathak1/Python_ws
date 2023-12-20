import turtle 
import time
my_turtle=turtle.Turtle()
def print_pyramid(rows:int)->None:
    colours = ["white","black","red","green","blue","cyan","magenta","yellow","orange","purple","brown","pink","gray","lightgray","darkgray"]
    my_turtle.speed("fastest")
    x_cord, y_cord = -100, 200
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            my_turtle.penup()
            my_turtle.goto(x_cord, y_cord)
            my_turtle.pendown()
            my_turtle.color(colours[i])
            my_turtle.write(i, font=("Aerial", 18, "bold"))
            x_cord += 30
        x_cord = -100
        y_cord -= 30
    my_turtle.hideturtle()
    turtle.bye()

def get_num_of_lines(name:str)->int :
    msg = f"Hi {name}, how many lines do you want  "
    num_of_rows = turtle.numinput(title="get rows",prompt=msg ,default = 10,minval = 1,maxval = 15)
    return  int(num_of_rows) 

def get_name()->str :
    msg = "What's your name"
    input_str = turtle.textinput(title="get name",prompt=msg)
    return input_str

name = get_name()
num_rows = get_num_of_lines(name)
print_pyramid(num_rows)
time.sleep(3)
