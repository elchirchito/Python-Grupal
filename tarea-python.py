import random

numero_secreto = random.randint(1, 100)
intentos = 0
maximo = 100
minimo = 1

print("bienvenido al juego de adivinar el numero!")
print(f"Tenes que adivinar un numero entre {minimo} y {maximo}")

adivinado = False 

while intentos < 5 and not adivinado:
    intento = int(input("ingresá tu numero: "))

    if intento == numero_secreto:
        print("wenaa, adivinaste el numero!")
        adivinado = True
    elif intento < numero_secreto:
        print("el numero es mayor.")
        minimo = intento + 1
    else:
        print("el numero es menor.")
        maximo = intento - 1

    intentos += 1
    print(f"te quedan {5 - intentos} intentos.")

if not adivinado:
    print(f"perdiste loko, el numero secreto era {numero_secreto}.")
