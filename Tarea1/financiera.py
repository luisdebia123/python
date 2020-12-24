class financiera:

    def __init__(self, nombre, id, saldo_institucional, clientes):
        self.sumatoria_lineas_credito = 0
        self.nombre = nombre
        self.id = id
        self.saldo_institucional = saldo_institucional
        self.clientes = list() #Al iniciar, las financieras no tienen clientes (en blanco)

    def agregar_clientes(self, cliente):
        #Si estamos dentro del 10% del saldo institucional, podemos agregar cliente.
        #como el cliente no existe para la financiera, asignamos al crear, la linea de credito.
        if self.sumatoria_lineas_credito <= 0.1 * self.saldo_institucional:
            cliente.financiera = self.nombre
            cliente.linea_credito = 1000000 # Asignamos a la línea de credito cliente un millón.
            self.clientes.append(clientes)  # lo guardamos en la lista clientes de la financiera.
        else:
            pass #aquí hay que agregar que pasa si no cumple.

    def eliminar_cliente(self, id_cliente):
        for index, cliente in enumerate(self, clientes):
            if cliente.id == id_cliente:
                self.clientes.remove(index)
                break
    
    def transferir(self, id_origen, id_destino, monto):
        if id_origen == self.id:
            origen = self
        elif id_destino == self.id:
            destino = self
        cliente_origen_encontrado = False   #inicializo en "false" para evaluarlas.
        cliente_destino_encontrado = False 
        for cliente in self.clientes:
            if cliente.id == id_origen:
                origen = cliente
                cliente_origen_encontrado = True
            if cliente.id == id_destino:
                destino = cliente
                cliente_destino_encontrado = True
            if (cliente_destino_encontrado = True 
                and cliente_origen_encontrado == False):
                raise Exception ("El origen no se encontró")
            elif (cliente_destino_encontrado = False 
                and cliente_origen_encontrado == True):
                raise Exception ("El destino no se encontró")
            elif (cliente_destino_encontrado = False 
                and cliente_origen_encontrado == False):
                raise Exception ("El origen y destino no se encontró")
            else:
                if isinstance(origen, cliente):
                    if (origen.saldo + origen.linea_credito) >= monto:
                        if isinstance(destino, cliente)

        
