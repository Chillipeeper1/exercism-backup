def rows(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n < 0:
        raise ValueError("number of rows is negative")
    else:
        triangulo = rows(n - 1)
        
        fila_anterior = triangulo[-1]
        
        nueva_fila = [1]
        
        for i in range(len(fila_anterior) - 1):
            suma = fila_anterior[i] + fila_anterior[i+1]
            nueva_fila.append(suma)
            
        nueva_fila.append(1)
        
        triangulo.append(nueva_fila)
        
        return triangulo
