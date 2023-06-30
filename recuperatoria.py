op=int(input("ingrese una opcion"))
while op>4:
    print("opcion invalida")
    op=int(input("ingrese una opcion"))
print("----regiistro de ciudadanos de la union europea----")
print("1.Grabar")
print("2.Buscar")
print("3.Imprimir certificado")
print("4.Salir")

if op==1:
    print("ha ingresado la opcion 1")
elif op==2:
    print("buscar informacion")
elif op==3:
    print("imprimir certificado") 
elif op==4:
    print("salir")      

class Persona:
    def __init__(self, nif, nombre, edad, pertenece_ue):
        self.nif = nif
        self.nombre = nombre
        self.edad= edad
        self.pertenece_ue = pertenece_ue

def __str__(self):
    return f"NIF:{self.nif} \n nombre:{self.nombre}\nEdad: {self.edad}\npertenece a la union europea{self.pertenece_ue}"

def verificar_nif(nif):
    if len(nif)!= 20 or not nif[:8].isdigit() or nif[8] != "-"or not nif[9].isalnum():
        return False
        return True

def grabar_persona(personas):
    nif = input("ingrese el NIF")
    while not verificar_nif(nif):
        print("el NIF ingresado es incorrecto.")
        nif = input("ingrese el nif nuevamente:")
        nombre = input("ingrese el nombre:")
        while len(nombre) <8:
            print("el nombre debe tener minimo caracteres.")
        nombre = input("ingrese nombre nuevamente.")
        edad = int(input("ingrese la edad:"))
        while edad <0:
            print("la edad debe ser mayor o igual a 0")
            edad = int(input("ingrese la edad nuevamente;"))
            pertenece_ue = input("¿pertenece a la union europea? (S/N): ").upper() == "S"
            persona = persona(nif, nombre, edad, pertenece_ue)
            personas.append(persona)
            print("persona grabada exitosamente.")

def buscar_persona(persona):
    nif = input("ingrese el NIF de la persona a buscar:")
    for persona in persona:
        if persona.nif == nif:
            print(persona)
            if persona.pertenece_ue:
                print("la persona pertenece a la union europea.")
            else:
                print("la persona no pertenece a la union europea.")
                return
                print("no se encontro ninguna persona con el NIF especificado.")

def imprimir_certificados(personas):
    for personas in personas:
        print("certificado de nacimiento:")
        print(f"nombre: {Persona.nombre}")
        print(f"NIF:{Persona.nif}")
        print()

        print("certificado de pertenencia a la union europea:")
        print(f"Nombre: {Persona.nombre}")
        print(f"NIF: {Persona.nif}")
        if Persona.pertenece_ue:
            print("la persona pertenece a la union europea.")
        else: 
            print("la persona no pertenece a la union europea.")
            print()
