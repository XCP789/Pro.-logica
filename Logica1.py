
estudintes = {
    "Doris":["POO", "calculo"], 
    "Marco":["calculo"], 
    "Maria":["POO", "calculo"]
}

profesores = {
    "Prof. tirado":["POO"], 
    "Prof. Abraham":["calculo"]
}

materias = {
    "POO": True,
    "calculo": True  
}

lugares = {
    "Biblioteca": True,
    "Lab. Cómputo": True
}

U=["Doris", "Marco", "Maria", "Prof. tirado", "Prof. Abraham", "POO", "Cálculo", "Biblioteca", "Lab. Cómputo"]

relacion_aprueba = {("Maria", "Calculo")}
relacion_reprueba = {("marco", "POO")}

def Estudiantes(x):
    return x in estudintes

def Profesores(x):
    return x in profesores

def Materias(x):
    return x in materias

def Lugares(x):
    return x in lugares

def Aprueba(x, y):
    return (x, y) in relacion_aprueba

def Reprueba(x, y):
    return (x, y) in relacion_reprueba

#confirma que el dato del profesor sea real y tamboién que la materia que imparte sea la misma que en su universo 
def Imparte(x, y):
    if Profesores(x):
        return y in profesores[x] #si x (profesor) tiene la y (materia) que tiene en el universo 
    return False

print("\n1.- Estudiante(x)")
print(f"x=Doris; Estudiante('Doris') = {Estudiantes('Doris')}")
print(f"x=POO; Estudiante('POO') = {Estudiantes('POO')}")

print("\n2.- Docente(x)")
print(f"x=Tirado; Docente('Prof. tirado') = {Profesores('Prof. tirado')}")
print(f"x=marco; Docente('marco') = {Profesores('marco')}")

print("\n3.- Materia(x)")
print(f"x=POO; Materia('POO') = {Materias('POO')}")
print(f"x=Maria; Materia('Maria') = {Materias('Maria')}")

print("\n4.- Lugar(x)")
print(f"x=Biblioteca; Lugar('Biblioteca') = {Lugares('Biblioteca')}")
print(f"x=POO; Lugar('POO') = {Lugares('POO')}")

print("\n5.- Aprueba(x, y)")
print(f"x=Maria; y=Calculo; Aprueba('Maria', 'Calculo') = {Aprueba('Maria', 'Calculo')}")
print(f"x=Marco; y=Calculo; Aprueba('Marco', 'Calculo') = {Aprueba('Marco', 'Calculo')}")


print("\n6.- Reprueba(x, y)")
print(f"x=marco; y=POO; Reprueba('marco', 'POO') = {Reprueba('marco', 'POO')}")
print(f"x=Biblioteca; y=POO; Reprueba('Biblioteca', 'POO') = {Reprueba('Biblioteca', 'POO')}")


print("\n7.- Imparte(x, y)")
print(f"x=Prof. tirado; y=POO; Imparte('Prof. tirado', 'POO') = {Imparte('Prof. tirado', 'POO')}")
print(f"x=Prof. tirado; y=calculo; Imparte('Prof. tirado', 'calculo') = {Imparte('Prof. tirado', 'calculo')}")