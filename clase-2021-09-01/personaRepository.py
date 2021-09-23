from persona import Persona


class PersonaRepository:

    def __init__(self):
        self.personas = {}
        self.lastPersonaId = 0
        self.readFile()

    def readFile(self):
        # Leo todos registros del archivo de texto
        with open('persona.txt', 'r') as file:
            for line in file:
                pseudoPersona = line[:-1].split(';;')
                self.personas[int(pseudoPersona[0])] = Persona(
                    personaId=int(pseudoPersona[0]), nombre=pseudoPersona[1], apellido=pseudoPersona[2])
                self.lastPersonaId = int(pseudoPersona[0])

    def writeFile(self):
        # Escribo todos los registros en el archivo de texto
        with open('persona.txt', 'w') as file:
            for persona in self.personas.values():
                file.write('{};;{};;{}\n'.format(
                    persona.personaId, persona.nombre, persona.apellido))

    # Leer todos los registros
    def findAll(self):
        return list(self.personas.values())

    # Leer un registro por el id
    def findByPersonaId(self, personaId: int):
        if personaId not in self.personas:
            raise KeyError('Clave Inexistente')
        return self.personas[personaId]

    # Leer el último registro
    def findLast(self):
        return list(self.personas.values())[-1]

    # Agregar un registro nuevo
    def add(self, persona: Persona):
        if persona.personaId in self.personas:
            raise KeyError('Clave Existente')
        self.lastPersonaId += 1
        persona.personaId = self.lastPersonaId
        self.personas[persona.personaId] = persona
        return persona

    # Modificar un registro existente
    def update(self, newPersona: Persona, personaId: int):
        if personaId not in self.personas:
            raise KeyError('Clave Inexistente')
        self.personas[personaId] = newPersona
        return self.personas[personaId]

    # Eliminar un registro existente
    def delete(self, personaId: int):
        del self.personas[personaId]


