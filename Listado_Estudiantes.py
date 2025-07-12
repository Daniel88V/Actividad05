class Estidiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final
        self.estudiante = []
    def ingreso_estudiante(self, estudiante):
        self.estudiante.append(estudiante)
        print(f"Estudiante {self.nombre} ingresado correctamente")
    def __str__(self):
        return f"Alumno: {self.nombre}| Carné: {self.carne}| Carrera: {self.carrera}| Nota final: {self.nota_final}"
class Clase:
    def __init__(self, grado):
        self.nombre = grado
        self.estudiante = []
    def encontrar_estudiante(self, carne):
        for estudiante in self.estudiante:
            if estudiante.carne == carne:
                return estudiante
        return None
    def ingreso_estudiante(self):
        print(f"---Listado de estudiantes---")
        nombre = input("Ingrese el nombre del estudiante: ")
        carne = input("Ingrese el carné del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        nota = input("Ingrese el nota final del estudiante: ")
        if self.encontrar_estudiante(carne):
            print("Error, este estudiante ya se encuentra en la lista")
            return

def main():
    print(" ===BIENVENIDO AL MENÚ===")
    print("Seleccione una opción")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar listado de estudiantes")
    print("3. Buscar estudiante (por carné)")
    print("4. Calcular promedio de todos los estudiantes")
    print("5. Salir")
if __name__ == "__main__":
    main()