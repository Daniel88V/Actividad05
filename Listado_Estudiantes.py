class Estidiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

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