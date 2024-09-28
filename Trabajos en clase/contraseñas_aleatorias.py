import random
import string

def contrasena_random(longitud):
    caracteres=string.ascii_letters+string.digits+string.punctuation
    contrasena="" .join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    try: 
        
        longitud=int (input("De cuantos caracteres desea la contraseña: "))
        if longitud <1:
            print("la contraseña debe ser un numero mayor a 1")
        else:
            contrasena=contrasena_random(longitud)
        print("la contraseña generada es ", contrasena)
    except ValueError:
        print("por favor, introduce un numero valido")
if __name__=="__main__":
    main()
