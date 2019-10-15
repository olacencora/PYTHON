import math

def area_calculate( a, b, c ):
    perimeter = float
    perimeter = a + b + c

    print("Obwód trójkąta to: " + str( perimeter ))

    p = float
    p = perimeter / 2

    print("połowa obdwodu trójkąta to:" + str(p))

    z = float
    z = (p * (p - a) * (p - b) * (p - c))

    print("składowa wyniku pola to:" + str(z))

    area = float
    area = math.sqrt(z)

    return(print("Pole trójkąta to:" + str(area)))


def check_triangle_angle( a, b, c):
    if math.pow( a,2 ) + math.pow( b,2 ) == math.pow( c,2 ) or math.pow( c,2 ) + math.pow( b,2 ) == math.pow( a,2 ) or math.pow( c,2 ) + math.pow( a,2 ) == math.pow( b,2 ):
        print("trójkąt jest prostokątny")
    elif math.pow( a,2 ) + math.pow( b,2 ) < math.pow( c,2 ) or math.pow( c,2 ) + math.pow( b,2 ) < math.pow( a,2 ) or math.pow( c,2 ) + math.pow( a,2 ) < math.pow( b,2 ):
        print("trójkąt jest rozwartokątny")
    else:
        print("trójkąt jest ostrokątny")

def check_triangle_side( a, b, c ):
    if a == b == c:
        print("trójkąt jest równoboczny")
    elif a == b or a == c or c == b:
        print("trójką jest równoramienny")
    else:
        print("trójkąt jest różnoboczny")


a = float (input("podaj pierwszą zmienną a = "))
b = float (input("podaj drugą zmienną b = "))
c = float (input("podaj trzecią zmienną c = "))

if (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
    area_calculate(a, b, c)
    check_triangle_angle(a, b, c)
    check_triangle_side(a, b, c)
else:
    print("podane boki nie spełniają warunku zbudowania trójkąta")

