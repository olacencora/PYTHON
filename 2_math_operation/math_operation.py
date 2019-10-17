
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
print("wyrażenie w liście to: " + str(list_equation))

# sprawdzam na której pozycji jest "=" w równaniu
equal_position = list_equation.index("=")
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
print("lewa strona równania to: " + str(left_side))
print("prawa strona równania to: " + str(right_side))

# sprawdzam liczbę przed x
x_position = list_equation.index("x")
print(x_position)
if x_position == 0:
    numb_before_x = 1
else:
    numb_before_x = list_equation[x_position - 1]
print("liczba przed x to: " + str(numb_before_x))

# funkcja sprawdzająca liczbę obok x

def check_numb_next_x_right():
    for i in right_side:
        if (i != "x") and (i != numb_before_x) and (i != "+") and (i != "-"):
            numb_next_x = i
        else:
            numb_next_x = 0
    print("x znajduje sie po prawej stronie i wynosi:" + str(numb_next_x))
    return numb_next_x

def check_numb_next_x_left():
    for i in left_side:
        if (i != "x") and (i != numb_before_x) and (i != "+") and (i != "-"):
            numb_next_x = i
        else:
            numb_next_x = 0
    print("x znajduje sie po lewej stronie a liczba obok wynosi: " + str(numb_next_x))
    return numb_next_x

# sprawdzam po ktorej stronie wyrazenia jest "x" i wywołuje funkcję zanajdującą liczbe obok x
int = numb_next_x = 0
for i in left_side:
    if (i == "x"):
        check_numb_next_x_left()
        numb_opposite_x = right_side[0]
    else:
        for i in right_side:
            if (i == "x"):
                check_numb_next_x_right()
                numb_opposite_x = left_side[0]
print("liczba po przeciwnej stronie rownania do x to: " + str(numb_opposite_x))

#sprawdzam znak przed numb next to x
numb_next_x_position = list_equation.index(numb_next_x)
if numb_next_x == 0:
    sign_numb_before_x = ""
else:
    sign_numb_next_x = list_equation[numb_next_x - 1]
print("znak przed liczba obok x to: " + str(sign_numb_before_x))

# zmieniam str na int

int(numb_before_x)
int(numb_opposite_x)
int(numb_next_x)

# wyliczam x
if sign_numb_before_x == "":
    find_numb = numb_opposite_x / numb_next_x
elif sign_numb_before_x == "+":
    find_numb = (numb_opposite_x - numb_next_x) / numb_next_x
else:
    find_numb = (numb_opposite_x + numb_next_x) / numb_next_x
print("x =" + str(find_numb))
