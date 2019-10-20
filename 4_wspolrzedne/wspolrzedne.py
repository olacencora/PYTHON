import math

# definiuje funkcje obliczajce kolejno parametr kierunkowy i dlugosc odcinkow zaokraglona do dwoch miejsc poprzecinku
def get_direction_parameter(first_x, first_y, second_x, second_y):
    if first_x - second_x == 0:
        direction_parameter = 0
    else:
        direction_parameter = (first_y - second_y)/(first_x - second_x)
    return direction_parameter

def get_line_lenght(first_x, first_y, second_x, second_y):
    numb_1 = math.sqrt((second_x - first_x)**2 + (second_y - first_y)**2)
    line_lenght = round(math.fabs(numb_1), 2)
    return line_lenght


point_a_x = float(input("podaj warosc x punktu A: "))
point_a_y = float(input("podaj warosc y punktu A: "))
point_b_x = float(input("podaj warosc x punktu B: "))
point_b_y = float(input("podaj warosc y punktu B: "))
point_c_x = float(input("podaj warosc x punktu C: "))
point_c_y = float(input("podaj warosc y punktu C: "))
point_d_x = float(input("podaj warosc x punktu D: "))
point_d_y = float(input("podaj warosc y punktu D: "))

direction_parameter_ab = get_direction_parameter(point_a_x, point_a_y, point_b_x, point_b_y)
print("parametr kierunkowy prostej AB to : " + str(direction_parameter_ab))
line_lenght_ab = get_line_lenght(point_a_x, point_a_y, point_b_x, point_b_y)
print("długość odcinka AB to : " + str(line_lenght_ab))

direction_parameter_bc = get_direction_parameter(point_b_x, point_b_y, point_c_x, point_c_y)
print("parametr kierunkowy prostej BC to : " + str(direction_parameter_bc))
line_lenght_bc = get_direction_parameter(point_b_x, point_b_y, point_c_x, point_c_y)
print("długość odcinka BC to : " + str(line_lenght_bc))

direction_parameter_cd = get_direction_parameter(point_c_x, point_c_y, point_d_x, point_d_y)
print("parametr kierunkowy prostej CD to : " + str(direction_parameter_cd))
line_lenght_cd = get_direction_parameter(point_c_x, point_c_y, point_d_x, point_d_y)
print("długość odcinka CD to : " + str(line_lenght_cd))

direction_parameter_da = get_direction_parameter(point_d_x, point_d_y, point_a_x, point_a_y)
print("parametr kierunkowy prostej DA to : " + str(direction_parameter_da))
line_lenght_da = get_direction_parameter(point_d_x, point_d_y, point_a_x, point_a_y)
print("długość odcinka DA to : " + str(line_lenght_da))

perpondicular_ab_bc = round((direction_parameter_ab * direction_parameter_bc), 0)
print(perpondicular_ab_bc)
perpondicular_bc_cd = round((direction_parameter_bc * direction_parameter_cd), 0)
print(perpondicular_bc_cd)
perpondicular_cd_da = round((direction_parameter_cd * direction_parameter_da), 0)
print(perpondicular_cd_da)
perpondicular_da_ab = round((direction_parameter_da * direction_parameter_ab), 0)
print(perpondicular_da_ab)

if direction_parameter_ab == direction_parameter_cd and direction_parameter_bc == direction_parameter_da and line_lenght_da == line_lenght_ab:
    print("figura to kwadrat")
elif perpondicular_da_ab == -1 and perpondicular_bc_cd and perpondicular_bc_cd == -1 and direction_parameter_ab == direction_parameter_cd:
    print("figura to prostokąt")
elif direction_parameter_ab == direction_parameter_cd and direction_parameter_bc == direction_parameter_da:
    print("figura to równoległobok")
elif direction_parameter_ab == direction_parameter_cd or direction_parameter_bc == direction_parameter_da:
    print("figura to trapez")