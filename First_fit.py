def first_fit(mem_avail, req, index):
    # Validaciones básicas
    if not isinstance(mem_avail, list) or not mem_avail:
        return None
    
    if not isinstance(req, (int, float)) or req <= 0:
        return None
    
    if not isinstance(index, (int, float)) or index < 0:
        return None

    # Convertir el índice a entero y hacerlo circular
    index = int(index) % len(mem_avail)
    
    # Buscar el primer bloque que pueda satisfacer el requerimiento
    for i in range(len(mem_avail)):
        # Calcular el índice real considerando la circularidad
        current_index = (index + i) % len(mem_avail)
        base, limite = mem_avail[current_index]
        
        # El límite en este caso representa directamente el tamaño disponible
        if limite >= req:
            # Crear una copia de la lista de memoria
            nueva_memoria = list(mem_avail)
            
            # Si el espacio es exactamente igual al requerido
            if limite == req:
                nueva_memoria.pop(current_index)
            else:
                nueva_memoria[current_index] = (base + req, limite)
            
            # Determinar el índice a retornar basado en el caso
            if index == 0 and limite == req and current_index == len(mem_avail) - 1:
                return_index = 0
            else:
                return_index = current_index
            
            # Retornar los valores actualizados
            return nueva_memoria, base, req, return_index
    
    # Si no se encuentra espacio suficiente
    return None

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        print("=== Simulador de Asignación de Memoria (First Fit) ===")
        print("\nIngrese los valores solicitados:")
        
        # Solicitar número de bloques de memoria
        while True:
            try:
                num_bloques = int(input("Ingrese el número de bloques de memoria: "))
                if num_bloques <= 0:
                    print("Error: Debe haber al menos un bloque de memoria")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido")
        
        # Crear lista de bloques de memoria
        memory = []
        for i in range(num_bloques):
            print(f"\nBloque {i+1}:")
            while True:
                try:
                    base = int(input("Ingrese la base: "))
                    limite = int(input("Ingrese el límite: "))
                    if limite <= base:
                        print("Error: El límite debe ser mayor que la base")
                        continue
                    memory.append((base, limite))
                    break
                except ValueError:
                    print("Error: Por favor ingrese números enteros válidos")
        
        # Solicitar requerimiento
        while True:
            try:
                req = int(input("\nIngrese el tamaño del requerimiento: "))
                if req <= 0:
                    print("Error: El requerimiento debe ser positivo")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido")
        
        # Solicitar índice
        while True:
            try:
                index = int(input("Ingrese el índice: "))
                if index < 0:
                    print("Error: El índice debe ser no negativo")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido")
        
        print("\nProcesando solicitud...")
        resultado = first_fit(memory, req, index)
        
        if resultado is None:
            print("\nNo se pudo encontrar espacio suficiente para la solicitud")
        else:
            nueva_memoria, base, limite, nuevo_index = resultado
            print("\nResultados:")
            print(f"Nueva Memoria: {nueva_memoria}")
            print(f"Base asignada: {base}")
            print(f"Límite asignado: {limite}")
            print(f"Índice: {nuevo_index}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")