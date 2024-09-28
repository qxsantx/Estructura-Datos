peso=float(input("cuanto es tu peso en kg?: 60"))
alt=float(input("cuanto es tu altura en metros:? "))
imc=peso/(alt**2)
print("tu indice de masa corporal es",imc)
if imc<18.5:
    print("estas bajo de peso")
elif imc>=18.5 and imc<=24.9:
    print("estas en un peso normal")
elif imc<24.0 :
    print("estas en sobrepeso")