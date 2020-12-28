import uuid
import os
os.system('cls')

class Financiera:

    def __init__(self, nombre, id, saldo_institucional):
        self.nombre = nombre
        self.id = id
        self.saldo_institucional = saldo_institucional
        self.clientes =[]
        self.suma_linea_credito = 0 

    def agregar_cliente(self, nombre, id, monto_ingresado):
    
            self.clientes.append(nombre)
            self.clientes.append(id)
            self.clientes.append(monto_ingresado)
            self.suma_linea_credito += 1000000
            return self.clientes

    def eliminar_cliente(self, nombre, id, monto_ingresado):
        self.clientes.remove(nombre)
        self.clientes.remove(id)
        self.clientes.remove(monto_ingresado)
        return self.clientes

    def transferir(self,cliente_origen,cliente_destino,monto):
        origen = 0
        destino = 0
        pos=0
        origen_encontrado = ""
        destino_encontrado = ""
        # valida si existe el cliente de origen
        for x in elegir.clientes:
            if cliente_origen == (x):
                origen=pos              # marca  origen co el indice pos
                pos=pos+1
                origen_encontrado = "S" # oringen_encontrado = S
            elif cliente_destino == (x):
                destino=pos
                pos=pos+1
                destino_encontrado = "S" # destino encontrado = S
            else :
                pos=pos+1
        if origen_encontrado == "S" and destino_encontrado == "S" and monto <= (elegir.clientes[origen+2]):
            elegir.clientes[origen+2] -= monto
            elegir.clientes[destino+2] += monto
#################################################################################
#          Procesa Transferencia entre Financieras
#################################################################################

    def Inter_Transferencia(self,f2,cliente_origen,cliente_destino,monto_transferido):
            origen = 0
            destino = 0
            pos=0
            origen_encontrado = ""
            destino_encontrado = ""
            

            # valida si existe el cliente de origen
            for y in f1.clientes:
                if cliente_origen == (y):
                    origen=pos              # marca  origen co el indice pos
                    pos=pos+1
                    origen_encontrado = "S" # oringen_encontrado = S
                else :
                    pos = pos + 1
                    poss=0
            for n in f2.clientes:
                if cliente_destino == (n):
                    destino=poss              # marca  indece destino a modificar con el indice pos
                    poss=poss+1
                    destino_encontrado = "S" # oringen_encontrado = S
                else :
                    poss = poss + 1
            if origen_encontrado == "S" and destino_encontrado == "S":
                f1.clientes[origen+2] -= monto_transferido
                f2.clientes[destino+2] += monto_transferido
        
        
#def giros_totales():

#def abonos_totales():

#def mostrar_saldo_institucional():




# Agregar Clientes #

el_prestamo = Financiera("El Prestamo",uuid.uuid4(),100000000)
el_prestamo_2 = Financiera("El Prestamo_2",uuid.uuid4(),100000000)

# Ingreso clientes a el_prestamo
el_prestamo.agregar_cliente("El Rey",uuid.uuid4(), 5000000)
el_prestamo.agregar_cliente("La Reina", uuid.uuid4(), 1000000)
el_prestamo.agregar_cliente("El Principe",uuid.uuid4(), 61000000)
el_prestamo.agregar_cliente("La Princesa",uuid.uuid4(),1060000)
el_prestamo.agregar_cliente("La Princesita",uuid.uuid4(),10200000)

# Ingreso clientes a el_prestamo2
el_prestamo_2.agregar_cliente("Pedro",uuid.uuid4(), 1000000)
el_prestamo_2.agregar_cliente("Rosita", uuid.uuid4(), 2000000)
el_prestamo_2.agregar_cliente("Rolando",uuid.uuid4(), 3000000)
el_prestamo_2.agregar_cliente("Juan Arancibia",uuid.uuid4(),400000)
el_prestamo_2.agregar_cliente("Luis Debia",uuid.uuid4(),5000000)

print("***************** Lista Clientes Ingresados el_prestamo_2 *********************")
# Listar Clientes
print()

a=0
b=1
c=2
n=int((len(el_prestamo_2.clientes)/3))
for recorrer  in range(n):
    print("el Nombre de Cliente es  :",el_prestamo_2.clientes[a],el_prestamo_2.clientes[b],el_prestamo_2.clientes[c])
    a=a+3
    b=b+3
    c=c+3
print()
print ("-126---------------------------------------------------------------------------")
print("*****************Lista Clientes Ingresados el_prestamo *********************")
print()
a=0
b=1
c=2
n=int((len(el_prestamo.clientes)/3))
for recorrer  in range(n):
    print("el Nombre de Cliente es  :",el_prestamo.clientes[a],el_prestamo.clientes[b],el_prestamo.clientes[c])
    a=a+3
    b=b+3
    c=c+3

# Eliminar Clientes   ##############################################


# se digita el cliente a eliminar
cliente_a_eliminar = "Pedro"

# Se digita la financiera correspondiente al cliente
elegir = el_prestamo_2     
a=0
y=0
n=int((len(elegir.clientes)))
while y <= n:
    if elegir.clientes[a] == cliente_a_eliminar :
        print()
        print("el Nombre de Cliente a eliminar  :",elegir.clientes[a],elegir.clientes[a+1],elegir.clientes[a+2])
        y=n
        nombre = elegir.clientes[a]
        id = elegir.clientes[a+1]
        monto_ingresado = elegir.clientes[a+2]
        elegir.eliminar_cliente(nombre, id, monto_ingresado)
    else:
        y = y + 1
        a = a + 1


###########################################
print ()
print("Lista Actualizada")
print ("-----------------")
print ()

a=0
b=1
c=2
n=int((len(el_prestamo_2.clientes)/3))
for recorrer  in range(n):
    print("el Nombre de Cliente es  :",el_prestamo_2.clientes[a],el_prestamo_2.clientes[b],el_prestamo_2.clientes[c])
    a=a+3
    b=b+3
    c=c+3
print()
# Se ingresa clientes misma Financiera
elegir.transferir('Rosita','Rolando',1)

# Se Ingresa tranferencia entre Financiera
f1 = el_prestamo_2
f2 = el_prestamo

f1.Inter_Transferencia(f2,'Juan Arancibia','El Principe',1)

# Lista Clientes Financiera el_prestamo
print()
print (" Lista Clientes Financiera el_prestamo ")
print ("---------------------------------------")
a=0
b=1
c=2
n=int((len(el_prestamo.clientes)/3))
for recorrer  in range(n):
    print("el Nombre de Cliente es  :",el_prestamo.clientes[a],el_prestamo.clientes[b],el_prestamo.clientes[c])
    a=a+3
    b=b+3
    c=c+3

# Lista Clientes Financiera elprestamo_2
print()
print("Lista Clientes Financiera el_prestamo_2")
print("--------------------------------------")
a=0
b=1
c=2
n=int((len(el_prestamo_2.clientes)/3))
for recorrer  in range(n):
    print("el Nombre de Cliente es  :",el_prestamo_2.clientes[a],el_prestamo_2.clientes[b],el_prestamo_2.clientes[c])
    a=a+3
    b=b+3
    c=c+3
