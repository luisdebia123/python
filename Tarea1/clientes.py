from uuid import uuid4

class Cliente:
# "self.__saldo" es Saldo Privado. En caso de error, cambiarlo a "self.saldo"

    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.__saldo = saldo  #self.__saldo es para "saldo privado" de cada cliente.

    def girar (self, monto):
        self.__saldo -= monto
        return self.__saldo

    def abonar (self, monto):
        self.__saldo += monto
        return self.__saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
