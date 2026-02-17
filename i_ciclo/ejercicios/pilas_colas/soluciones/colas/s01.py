if __name__ == "__main__":
    # Cola definida
    cola = [1, 2, 3, 4, 5]
    
    print(f"Lista: {cola}")
    
    # Se desencola y encola en la misma línea
    cola.append(cola.pop(0))
    
    # Se imprime el resultado con espacios en blanco
    for n in cola:
        print(n, end=" ")