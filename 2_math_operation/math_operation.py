
#pobieram rówanie od uzytkownika
input_data = (input("napisz równanie z jedną niewiadomą użyj liczb całkowitych (dozwolone działanie: dodawanie, odejmowanie lub mnożenie np. 2x + 1 = 3) : "))

#konweruje podane wyrażenie na stringa
str(input_data)

#usuwam spacje
no_whitespaces = input_data.replace(" ", "")
print(no_whitespaces)

# equal_sign = no_whitespaces.find("=")
# print(equal_sign)

#metodą list comprehension wrzucam kazda litere stringa do listy
list_equation = [i for i in no_whitespaces]
print(list_equation)

# sprawdzam na której pozycji jest "=" w równaniu
equal_position = list_equation.index("=")
print(equal_position)
float(equal_position)
print(type(equal_position))

# dzielę wyrazenie na dwa oddzielone znakiem "="
# list_equation_left = [list_equation.index(i) > equal_position for i in list_equation]
# print(list_equation_left)
# list_equation_right = [float(i) < equal_position for i in list_equation]
# print(list_equation_right)
left_side=[]
right_side=[]

a = True
for i in list_equation:
    if i == "=":
        a = False
    elif a == True:
        left_side.append(i)
    else:
        right_side.append(i)
print(left_side)
print(right_side)

list_equation[1]
# sprawdzam liczbę przed x
x_position = list_equation.index("x")
print(x_position)
if x_position == 0:
    numb_before_x = 1
else:
    numb_before_x = list_equation[x_position - 1]

# funkcja sprawdzająca liczbę obok x
def check_numb_next_x_right():
    for i in list_equation_right:
        if (i != "x") and (i != numb_before_x) and (i != "+") and (i != "-"):
            numb_next_x = list_equation_right[i]
        else:
            numb_next_x = 0
    return numb_next_x

def check_numb_next_x_left():
    for i in list_equation_left:
        if (i != "x") and (i != numb_before_x) and (i != "+") and (i != "-"):
            numb_next_x = list_equation_left[i]
        else:
            numb_next_x = 0
    return numb_next_x

# sprawdzam po ktorej stronie wyrazenia jest "x" i wywołuje funkcję check_numb_next_x()
for i in left_side:
    if (i == "x"):
        check_numb_next_x()
    else:
        for i in list_equation_right:
            if (i == "x"):
                check_numb_next_x()

# sprawdzam liczbe