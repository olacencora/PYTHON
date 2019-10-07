import math

def areafunction( a, b, c ):
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

    return(print("pole trójkąta to:" + str(area)))


a = float (input("podaj pierwszą zmienną a = "))
b = float (input("podaj drugą zmienną b = "))
c = float (input("podaj trzecią zmienną c = "))

if (a <= 0) or (b <= 0) or (c <=0 ):
    print("podana wartość jest zła")
else:
    areafunction(a, b, c)


