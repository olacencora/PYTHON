print("==== START =====")
import string

data_input = "dwa plus dwa minus trzy plus siedem"

numbers_str = "zero jeden dwa trzy cztery pięć sześć siedem osiem dziewięć dziesiec".split(" ")
numbers_digits = list(string.digits)

operators_str = "plus minus podzielic pomnożyc".split()
operators_sign = "+  - / *".split()

print(numbers_str)
print(numbers_digits)

numbers = {}
for n_str, n_dig in zip(numbers_str, numbers_digits):
    numbers[n_str] = n_dig

print(numbers)

operators = {k: v for k, v in zip(operators_str, operators_sign)}
print(operators)

def mapper(data: str, map_data: dict):
    for k, v in map_data.items():
        data = data.replace(k, v)
    return data


# for k, v in numbers.items():
#     data_input = data_input.replace(k, v)
# data_input = mapper(data_input,numbers)


# for k, v in operators.items():
#     data_input = data_input.replace(k, v)
# data_input = mapper(data_input, operators)

data_input = mapper(data_input, {**numbers, **operators})

print(eval(data_input))
