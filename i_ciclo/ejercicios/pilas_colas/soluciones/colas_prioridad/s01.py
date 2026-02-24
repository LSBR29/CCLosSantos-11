# Función
def resta_numeros(numeros: list):
    nums = numeros.copy()       # Copia para no modificar la original
    
    while len(nums) > 1:
        nums = sorted(nums, reverse=True)   # Ordenar de Mayor a Menor
        a = nums.pop(0)     # Mayor
        b = nums.pop(0)     # Mayor
        
        diferencia = a - b
        
        if diferencia > 0:
            nums.append(diferencia)
    
    return nums[0] if nums else 0

# Main
if __name__ == "__main__":
    numeros = [2, 7, 4, 1, 8, 1]
    
    print(f"Números: {numeros}")
    print(f"Resultado final: {resta_numeros(numeros)}")