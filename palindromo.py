def es_palindromo(palabra):
    palabra=palabra.replace("", "").lower()
    return palabra==palabra[::-1]

while True:
    palabra=input("ingrese una palabra: ")
    if es_palindromo(palabra):
        print ( "la palabra", palabra , "es una palabra palindromo. ")
    else:
        print("la palabra ", palabra,  "no es una palabra palindromo. ")