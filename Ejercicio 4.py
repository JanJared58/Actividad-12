import sympy as sp

def main():
    
    x = sp.symbols('x')
    
    f = x**2 + 3*x + 2

    valor_usuario = input("Introduce un valor flotante para evaluar el límite de f(x) cuando x tiende a ese valor: ")
    try:
        punto = float(valor_usuario)
    except ValueError:
        print("El dato ingresado no es un número flotante válido.")
        return

    limite = sp.limit(f, x, punto)

    derivada = sp.diff(f, x)

    print(f"\nEl límite de f(x) cuando x tiende a {punto} es: {limite}")
    print(f"La derivada de f(x) es: {derivada}")

if __name__ == "__main__":
    main()
