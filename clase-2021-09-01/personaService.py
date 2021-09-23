from persona import Persona
from personaRepository import PersonaRepository


class PersonaService:

    def __init__(self):
        self.repository = PersonaRepository()

    def findAll(self):
        return self.repository.findAll()

    def findByPersonaId(self, personaId: int):
        try:
            return self.repository.findByPersonaId(personaId)
        except KeyError as e:
            print(e)

    def findLast(self):
        return self.repository.findLast()

    def add(self, persona: Persona):
        try:
            return self.repository.add(persona)
        except Exception as e:
            print(e)

    def update(self, persona: Persona):
        try:
            return self.repository.update(persona, persona.personaId)
        except Exception as e:
            print(e)

    def deleteByPersonaId(self, personaId: int):
        try:
            persona = self.repository.findByPersonaId(personaId)
            self.repository.delete(persona.personaId)
            return persona
        except Exception as e:
            print(e)

    def flush(self):
        self.repository.writeFile()


if __name__ == '__main__':
    service = PersonaService()
    personas = service.findAll()
    print(personas)
    persona = service.findByPersonaId(1)
    print(persona)
    persona = service.findLast()
    print(persona)
    persona = Persona(nombre='Oscar', apellido='Diaz')
    print(service.add(persona))
    persona.apellido='Días'
    print(service.update(persona))
    service.flush()
