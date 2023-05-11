
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
    for i, nombre in enumerate(nombres):
        if nombre in magos:
            nombres[i] = "El gran " + nombre


def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

magos = []
cientificos = []
sudamericanos = []

for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        sudamericanos.append(nombre)


grandes_magos = [nombre for nombre in magos]


print("Lista original:")
imprimir_nombres(nombres)
print()

print("Nombres de los grandes magos:")
imprimir_nombres(grandes_magos)

hacer_grandioso()




print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()


print("Sudamericanos:")
imprimir_nombres(sudamericanos)
print()

magos_grandiosos = [nombre for nombre in nombres if nombre.startswith("El gran")]

print("Nombres de los magos grandiosos:")
imprimir_nombres(magos_grandiosos)
print()
