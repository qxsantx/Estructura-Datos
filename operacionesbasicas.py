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
num2=float(input("digite otro numero: "))
operacion=(input("que operacion desea realizar? "))
resultado=operacion_basica(num1,num2,operacion)
print("su resultado es ", resultado)