from Rol import Rol
from Persona import Persona
from enum import Enum
from Lugar import Lugar

#Persona 1
persona1 = Persona('Lucia', 'Lopez', 'JPG', 'C:/Descargas/perfil.jpg')
persona1.setRol(Rol.MAESTRO)

lugar1 = Lugar("Plaza Fontabella", "Zona 10 ", " Telefono:66288600" )
lugar2 = Lugar("Museo de los Niños", "Zona 13 ", "Telefono:2213 8989")

persona1.addLugar(lugar2)
persona1.addLugar(lugar2)

#Persona2
persona2 = Persona('Pedro', 'Juarez', 'PNG', 'D:/Descargas/perfil.png')
persona2.setRol(Rol.ESTUDIANTE)

lugar1 = Lugar("USAC", "Zona 12", " Telefono:43002353" )
lugar2 = Lugar("Majadas", "Zona 11 ", "Telefono:89763834")

persona2.addLugar(lugar1)
persona2.addLugar(lugar2)

print(persona1)
print(persona2)
