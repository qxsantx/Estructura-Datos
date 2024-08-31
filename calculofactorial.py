def calculofactorial(numero:int)->str|int:
    resultado = 1
    if numero<0:
        return "no se puede numeros negativos"
    elif numero ==0:
        return 1
    for n in range (1,numero+1):
        resultado = resultado*n
    return resultado
while True:
    factorial=calculofactorial(int(input("digite un numero: ")))
    print("el resultado es", factorial)