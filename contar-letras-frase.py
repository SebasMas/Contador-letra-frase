Frase = input("Introduzca una frase: ")
Letra = input("Introduzca una letra: ")
contador = 0

for i in Frase:
    if i == Letra:
        contador += 1
print("La letra ",Letra," está ", contador," veces en la frase: ", Frase)
        
