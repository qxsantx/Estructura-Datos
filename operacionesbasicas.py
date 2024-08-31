def operacion_basica(num1,num2,operacion):
    if operacion=='+':
        return num1 + num2
    elif operacion=='-':
        return num1-num2
    elif operacion=='*':
        return num1*num2
    elif operacion=='/':
        if num2!=0:
            return num1/num2
        else:
            return "error division por cero"
    else:
        return "operacion no valida"
num1=float(input("digite un numero: "))
operacion=(input("que operacion desea realizar? "))
num2=float(input("digite otro numero: "))
resultado=operacion_basica(num1,num2,operacion)
print("su resultado es ", resultado)