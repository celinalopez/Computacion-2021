class Persona:

    def __init__(self, personaId=None, nombre='', apellido=''):
        self.personaId = personaId
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return '**({}) {}, {}**'.format(self.personaId, self.apellido, self.nombre)

