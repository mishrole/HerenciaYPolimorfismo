from Persona import Persona

class Estudiante(Persona):
    listaEstudiantes = []
    def __init__(self, nombre, apellido, id, curso):
        super().__init__(nombre, apellido)
        self.id = id
        self.curso = curso
        self.calificaciones = []
        
        Estudiante.listaEstudiantes.append(self)
    
    # Propio de Estudiante
    def asignaCalificacion(self, nota):
        self.calificaciones.append(nota)

    # Sobreescritura de método
    def informacion(self):
        super().informacion()
        print("Calificaciones", self.calificaciones)
    
    # Nuevo método de Estudiante
    # La intención es tener uno u otro
    # Como ya se sobreescribió arriba, al llamar informacion() ya está editado
    # def informacionEstudiante(self):
    #     self.informacion()
    #     print("Calificaciones", self.calificaciones)

    # Polimorfismo
    # En Python el método del padre no está implementado
    # Y se implementa en el hijo
    def informacionAbstracto(self):
        self.informacion()
        print(f"Cursos: {self.curso} | Calificaciones : {self.calificaciones}")

    @classmethod
    def imprimeListaEstudiantes(cls):
        for estudiante in cls.listaEstudiantes:
            estudiante.informacion()