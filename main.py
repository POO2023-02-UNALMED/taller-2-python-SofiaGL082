class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="blanco" or color=="negro"):
            self.color = color

class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados += 1

def cantidadAsientos(self):
    cant = 0
    for item in self.asientos:
        if item != None:
            cant += 1
    return cant

def verificarIntegridad(self):
    if self.registro == self.motor.registro:
        for asiento in self.asientos:
            if asiento != None:
                if self.registro != asiento.registro:
                    return "Las piezas no son originales"
        return "Auto original"
    else:
        return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, reg):
        self.registro = reg
    
    def asignarTipo(self, tMotor):
        if tMotor == "electrico" or tMotor == "gasolina":
            self.tipo = tMotor