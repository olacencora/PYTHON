data = "dwa plus dwa"
# result 4
numbers_str = "zero jeden dwa trzy cztery pięć sześć siedem osiem dziewięć".split(" ")
numbers_digits = list(string. digits)
print(numbers_str)
print(numbers_digits)


#numbers = {"jeden" : "1", "dwa" : "2"}
numbers = {}
for n_str, n_dig in zip(numbers_str, numbers_digits):
  #print(n_str + ":" + n_dig)
  numbers[n_str]=n_dig
print(numbers)

operators_str= "plus minus podzielić pomnożyć".split(" ")
operators_sign = "+ - / *".split(" ")

operators = { o_str: sign for o_str, sign in zip(operators_str, operators_sign)}
print(operators)

#zdefiniowanie typoów podpowiada a nie wymaga
def mapper(data: str, mapping_list: dict):
  for k, v in mapping_list.items():
  data = data.replace(k,v)
return data
#operators = {"plus" : "+"}

#for k, v in numbers.items():
  #data = data.replace(k,v)

data = mapper(data, numbers)
data = mapper(data, operators)

#mozna tez rozpakowac slowniki ** lub listy * czyli:
#data = mapper(data, {**numbers, **operators}) wyciaga te elementy z listy

#for k, v in operators.items():
  #data = data.replace(k,v)

print(eval(data)
