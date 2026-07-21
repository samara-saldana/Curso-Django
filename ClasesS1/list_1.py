"""
Crear una lista de Leads donde se utilicen los metodos apprend(), insert() y extend() para agregar elementos
asi mismo, usen u cclo para recorrer la lit y mostrsr los elementos de la misma

Usen los métodos sort() y reverse() para ordenar la lista y mostrarla en orden inverso
Usen los slices para mostrar los ´rimeros tres elementos de la lista y los ultimos 3 elementos de la lista
"""

lista_inicial = ["Carlos", "Ana", "Luis", "Marta"]

lista_inicial.append("Maria")

lista_inicial.insert(1,"Marcos")

otra_lista = ["Pedro", "Sofía ", "Juan"]
lista_inicial.extend(otra_lista)

for n in lista_inicial:
    # print(n)
    pass

lista_inicial.sort()

lista_inicial.reverse()
# print(lista_inicial)

# print(lista_inicial[:3],lista_inicial[-3:])




"""
Crear una tupla de estadis de Leads donde se puedan agregar elementos
asi mismo, usen u cclo para recorrer la lit y mostrsr los elementos de la misma

Usen los métodos sorted() y reverse() para ordenar la tupla y mostrarla en orden inverso
Usen los slices para mostrar los primeros tres elementos de la tupla y los ultimos 3 elementos de la tupla
Desempaquetar tuplas
"""

estados_leads = ("Nuevo", "Contactado", "Calificado", "Propuesta", "Cerrado")

estados_leads = estados_leads+("Finalizado", "Perido", "Rechazado")

for e in estados_leads:
    print(e)

estados_leads=sorted(estados_leads)
estados_leads=estados_leads[::-1]

print(estados_leads)

print(estados_leads[:3],estados_leads[-3:])

print("desempaquetado de tuplas")

nuevo, viejo, *_ =estados_leads



