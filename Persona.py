#Roles
from enum import Enum

class Rol(Enum):
    MAESTRO = 1
    ESTUDIANTE = 2

#Persona
class Persona:
    def __init__(self, nombre, apellido, tipoImagen, ubicacionImagen):
        self.nombre = nombre
        self.apellido = apellido
        self.tipoImagen = tipoImagen
        self.ubicacionImagen = ubicacionImagen
        self.rol = Rol.MAESTRO
        self.lugares = []

    def setRol(self, rol):
        self.rol = rol

    def addLugar(self, lugar):
        self.lugares.append(lugar)

    def __str__(self):
        return f"La persona {self.nombre}, con foto tipo {self.tipoImagen} ubicada en {self.ubicacionImagen}, \n tiene rol: {self.rol} \n lugares: [{','.join(map(str, self.lugares))}]"

    #Persona2
    def __init__(self, nombre, apellido, tipoImagen, ubicacionImagen):
        self.nombre = nombre
        self.apellido = apellido
        self.tipoImagen = tipoImagen
        self.ubicacionImagen = ubicacionImagen
        self.rol = Rol.MAESTRO
        self.lugares = []

    def setRol(self, rol):
        self.rol = rol

    def addLugar(self, lugar):
        self.lugares.append(lugar)

    def __str__(self):
        return f"La persona {self.nombre}, con foto tipo {self.tipoImagen} ubicada en {self.ubicacionImagen}, tiene rol: {self.rol} \n lugares: [{','.join(map(str, self.lugares))}]"
