from collections import deque

# Definimos las dimensiones de la matriz
rows, cols = 3, 3

# Función para verificar si una posición está dentro de los límites de la matriz
def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

# Función para convertir coordenadas de la matriz a un número en estilo row-major
def pos_to_num(x, y):
    return x * cols + y + 1

# Función para obtener los movimientos posibles desde una posición
def get_neighbors(x, y):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
    neighbors = []
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if is_valid(nx, ny):
            neighbors.append((nx, ny))
    return neighbors

# Implementación de la búsqueda por anchura
def bfs(start, goal):
    start_pos = (0, 0)  # Posición inicial (0, 0) que corresponde al número 1
    goal_num = goal  # Número de la posición final
    queue = deque([start_pos])
    visited = set()
    visited.add(start_pos)
    node_count = 0

    while queue:
        current_pos = queue.popleft()
        node_count += 1
        current_num = pos_to_num(*current_pos)
        
        # Verificar si hemos alcanzado el objetivo
        if current_num == goal_num:
            break

        for neighbor in get_neighbors(*current_pos):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return node_count

# Ejecutar la búsqueda por anchura desde el estado inicial 1 hasta el estado final 9
start = 1
goal = 9
total_nodes = bfs(start, goal)
print(f"Total de nodos en el árbol de búsqueda: {total_nodes}")
