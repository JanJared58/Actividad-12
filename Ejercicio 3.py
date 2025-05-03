import statistics

def main():
    numeros = []

    print("Por favor, ingresa 25 números enteros (uno por línea):")
    for i in range(25):
        while True:
            try:
                num = int(input(f"Ingrese el número {i+1} de 25: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número entero.")

    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    
    try:
        moda = statistics.mode(numeros)
    except statistics.StatisticsError:
        
        moda = "No existe una moda única"

    print("\nResultados:")
    print("Media:", media)
    print("Mediana:", mediana)
    print("Moda:", moda)

if __name__ == "__main__":
    main()
