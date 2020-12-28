import uuid
import os
os.system('cls')

class Cliente:
    nombre: str
    id: int
    saldo: float

    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo


    def girar(self, monto_giro):
        self.saldo = self.saldo - monto_giro
        return self.saldo

    def abonar(self, recibir_monto):
        self.saldo = self.saldo + recibir_monto
        return self.saldo

    def mostrar_saldo(self):
        return self.saldo

Luis = Cliente('Luis', uuid.uuid4, 1000000)
Juan = Cliente('Juan', uuid.uuid4, 51000)
Pedro = Cliente('Pedro', uuid.uuid4, 21000)
Felipe = Cliente('Felipe', uuid.uuid4, 11000)
Pablo = Cliente('Pablo', uuid.uuid4, 101000)



Luis.girar(500)
Luis.abonar(500)
Luis.abonar(1)

Juan.girar(450)
Juan.abonar(1400)

Juan.girar(5000)
Juan.abonar(40000)

Juan.girar(500)
Juan.abonar(600)

print ("Saldo de Clientes")
print ("cliente   :",( Luis.nombre," Saldo  :",Luis.mostrar_saldo() ) )
print ("cliente   :",( Juan.nombre," Saldo  :",Juan.mostrar_saldo() ) )
print ("cliente   :",( Pedro.nombre," Saldo  :",Juan.mostrar_saldo() ) )
print ("cliente   :",( Felipe.nombre," Saldo  :",Juan.mostrar_saldo() ) )
print ("cliente   :",( Pablo.nombre," Saldo  :",Juan.mostrar_saldo() ) )


