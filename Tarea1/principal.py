from Tarea1.financiera import financiera
from uuid import uuid4

if __name__ == "__main__":
    financiera_1 = financiera("La del Pato", 100000000)
    financiera_2 = financiera("Banco de Talca", 100000000)
    cliente_1 = cliente("Wolverine de las Mercedes", 500000)
    cliente_2 = cliente("Ciclope con Dos Ojos", 400000)
    cliente_3 = cliente("Snoopy Dog", 300000)
    cliente_4 = cliente("Perro Chocolo", 200000)
    cliente_5 = cliente("Piñera Culiao", 600000)
    cliente_6 = cliente("Gato con Botas", 700000)
    cliente_7 = cliente("Chancho con Chaleco", 800000)
    cliente_8 = cliente("Bebé Yoda", 900000)
    cliente_grupo_A = [cliente_1, cliente_2, cliente_3, cliente_4]
    cliente_grupo_B = [cliente_5, cliente_6, cliente_7, cliente_8]
    for clientes in clientes_grupo_A:
        financiera_1.agregar_clientes(cliente)

    for cliente in clientes_grupo_B:
        financiera_2.agregar_clientes(cliente)

def inprimir_clientes():
    for cliente in financiera_1.clientes:
        print(cliente.nombre, cliente.id, cliente.saldo)
    for cliente in financiera_2.clientes:
        print(cliente.nombre, cliente.id, cliente.saldo)
imprimir_clientes()

financiera_1.transferir(cliente_1.id, cliente_2.id, 300000)

