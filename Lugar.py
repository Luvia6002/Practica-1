class Lugar:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.direccion} - {self.telefono}"
        