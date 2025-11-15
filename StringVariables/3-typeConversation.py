#type conversation

number1 = input()
number2 = input()

a = type(int(number1))
result = number1 + number2
print(a)
print(result) # 20 30

result1 = int(number1) + int(number2)
print(result1) # 50

a = 12 # -> int
fl = float(a)

print(fl) # float -> 12.0

st = str(a)
print(st) # str -> 12
print(type(st)) # class 'str'
