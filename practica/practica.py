"""Ejercicio 1 · Quitar duplicados conservando el orden Dada 
ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"], 
obtén una lista sin repetidos respetando el orden de aparición 
(un set solo no alcanza)."""

ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil", "guayaquil"]
set = set()
ciudades_sin_repetidos = []
for ciudad in ciudades:
    if ciudad not in set:
        set.add(ciudad)
        ciudades_sin_repetidos.append(ciudad)
print(ciudades_sin_repetidos)

"""Ejercicio 2 · Contar con un diccionario
Con la misma lista, arma un diccionario {"Quito": 2, "Guayaquil": 2, "Cuenca": 1}"""
contador = {}
for ciudad in ciudades:
    if ciudad in contador:
        contador[ciudad] += 1
    else:
        contador[ciudad] = 1
print(contador)

mas_repetida = max(contador, key=contador.get)
print(mas_repetida)

"""Ejercicio 3 · 
Conjuntos en acción inscritos_matematica = {"Ana","Luis","Sol","Marco"} 
y inscritos_ingles = {"Luis","Marco","Ruth"}. 
Responde con código: ¿quiénes están en las dos?, 
¿quiénes solo en matemática?, ¿cuántos estudiantes distintos hay en total?"""

alumnos_matematica = {"Ana","Luis","Sol","Marco"}
alumnos_ingles = {"Luis","Marco","Ruth"}

en_ambas = alumnos_matematica & alumnos_ingles
solo_matematica = alumnos_matematica - alumnos_ingles
total_distintos = len(alumnos_matematica | alumnos_ingles)

print("Estudiantes en ambas materias:", en_ambas)
print("Estudiantes solo en matemática:", solo_matematica)
print("Total de estudiantes distintos:", total_distintos)

"""Ejercicio 4 · De lista de diccionarios a índice
Con clientes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Luis"}], 
crea un diccionario {id: cliente} para acceder por id sin recorrer 
la lista. Luego imprime el nombre del id 2."""

clientes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Luis"}]
indice_clientes = {cliente["id"]: cliente for cliente in clientes}
print(indice_clientes[2]["nombre"])

"""Ejercicio 5 · Tuplas como registros inmutables
Dada ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)], 
imprime el mes con mayor venta y el total, usando desempaquetado de tuplas."""

ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)]
total = sum(monto for _mes, monto in ventas)

mejor_mes, mejor_monto = max(ventas, key=lambda venta: venta[1])

print(f"Total: {total}")
print(f"Mejor mes: {mejor_mes} con {mejor_monto}")

for mes, monto in ventas:      
    print(f"{mes:<10} {monto}")