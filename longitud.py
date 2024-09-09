# Ultima version
def metros_a_pulgadas(metros):
    return metros * 39.37

def pulgadas_a_pies(pulgadas):
    return pulgadas / 12

# El bloque para hacer pruebas solo en este archivo
if __name__ == "__main__":
    print("Todo Correcto")
    # Ejemplo de uso del modulo longitud.py

metros = int(input("Ingrese la cantidad en metros: "))
pulgadas = metros_a_pulgadas(metros)
print(f"{metros} metros equivale a {pulgadas:.2f} pulgadas.")