# Definition of simple types

a = 1                     # int
b = 2.2                   # float
c = 3+2j                  # complex
d = (1,3,4,2.2)           # tuple / krotka
e = [1,2,3,4,5]           # lista 
f = {1,2,3,4,5}           # zbiór / set
g = {"A" : 1, "B" :[] }   # słownik, dict
h = "Testowa"             # string

# functions

f1=id(a)
f2=type(b)
f3=set()
f4=dict()
f5=list()
f6=tuple()

# string functions
string_func = dict()
string_func["capitalize()"]="Converts the first character to upper case"
string_func["casefold()"]="Converts string into lower case"
string_func["center()"]="Returns a centered string"
string_func["count()"]="Returns the number of times a specified value occurs in a string"
string_func["encode()"]="Returns an encoded version of the string"
string_func["endswith()"]="Returns true if the string ends with the specified value"
string_func["expandtabs()"]="Sets the tab size of the string"
string_func["find()"]="Searches the string for a specified value and returns the position of where it was found"
string_func["format()"]="Formats specified values in a string"
string_func["format_map()"]="Formats specified values in a string"
string_func["index()"]="Searches the string for a specified value and returns the position of where it was found"
string_func["isalnum()"]="Returns True if all characters in the string are alphanumeric"
string_func["isalpha()"]="Returns True if all characters in the string are in the alphabet"
string_func["isdecimal()"]="Returns True if all characters in the string are decimals"
string_func["isdigit()"]="Returns True if all characters in the string are digits"
string_func["isidentifier()"]="Returns True if the string is an identifier"
string_func["islower()"]="Returns True if all characters in the string are lower case"
string_func["isnumeric()"]="Returns True if all characters in the string are numeric"
string_func["isprintable()"]="Returns True if all characters in the string are printable"
string_func["isspace()"]="Returns True if all characters in the string are whitespaces"
string_func["istitle()"]="Returns True if the string follows the rules of a title"
string_func["isupper()"]="Returns True if all characters in the string are upper case"
string_func["join()"]="Joins the elements of an iterable to the end of the string"
string_func["ljust()"]="Returns a left justified version of the string"


while(True):
  print("=" * 20)
  print("String functions")
  print("=" * 20)
  print("Informacje o jakiej funkcji cię intresują? ")
  user_input = input()


  if not user_input.endswith("()"):
      user_input += "()"

  value = string_func.get(user_input)
  if value:
      print("Znaleziono definicję")
      print(20*"=")
      print("Function".ljust(15)+user_input)
      print(20*"-")
      print("Description".ljust(15)+value)
  else:
      print("Nie znaleziono definicji dla funcji " + user_input)
      print("Dostępne funkcje ")
      print(20*"=")
      for i in string_func.keys():
        print("->" +i)

