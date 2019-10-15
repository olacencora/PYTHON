# Zadanie 1 
# Obliczenie równania z jedną niewiadomą,
# a*)- niewiadmą jest x
# b)- wersja rozszerzona niewiadmą jest dowolna litera alfabetu
# ===========================================
# przykład
# input:
# "2x+10=12"
# output:
# "x=1"
# -------------------------------------------
# input:
# "2y+20=22"
# output:
# "y=1"

#pobieram rówanie od uzytkownika
equation = (input("napisz równanie z jedną niewiadomą (dozwolone działanie: dodawanie, odejmowanie lub mnożenie np. 2x + 1 = 3) : "))

#konweruje podane wyrażenie na stringa
#str(equation)

#usuwam spacje
equation.replace(" " , "")

#metodą list comprehension wrzucam kazda litere stringa do listy
list_equation = [i for i in equation]
print(list_equation)