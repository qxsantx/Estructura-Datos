control=0
cupo=int(input("ingrese cupo: "))
while control < cupo:
    valido= input("boleto valido ")
    if valido== "1":
        print("puede pasar ")
        control= control+1
    else: 
        print("no puede pasar ")
print("cupo lleno")