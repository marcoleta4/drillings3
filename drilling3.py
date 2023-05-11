
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]


def hacer_grandioso():
    magos = ["Harry Houdini", "David Blaine", "Teller"]
    for i in range(len(nombres)):
        if nombres[i] in magos:
            nombres[i] = "El gran " + nombres[i]


def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)


magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)


print("Lista original:")
imprimir_nombres(nombres)
print()


hacer_grandioso()

magos_grandiosos = [nombre for nombre in nombres if nombre.startswith("El gran")]


print("Nombres de los magos grandiosos:")
imprimir_nombres(magos_grandiosos)
print()


print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()


print("Otros nombres:")
imprimir_nombres(otros)
    