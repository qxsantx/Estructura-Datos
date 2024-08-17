x = float(input("digite un numero: "))
y = float(input("digite otro numero: "))
operacion = input("digite la operacion que desea realizar: ")

if operacion == '+':
  print(x + y)
elif operacion == '-':
  print(x - y)
elif operacion == '*':
  print(x * y)
elif operacion == '/':
  print(x / y)
else:
  print("operacion invalida")
