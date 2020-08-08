amigos = []

while len(amigos) < 5:
    nombre = input('Nombra un amigo: ')
    amigos.append(nombre)

lista_nombres = ', '.join(amigos)
print(f'Listado de amigos\n{lista_nombres}')
