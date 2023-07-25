import networkx as nx
import matplotlib.pyplot as plt

def metodo_dijkstra(grafo, nodo_inicial):
 
    distancia = {nodo: float('inf') for nodo in grafo.nodes}
    distancia[nodo_inicial] = 0
    visitados = set()
    predecesores = {nodo: None for nodo in grafo.nodes}

    while len(visitados) < len(grafo.nodes):
        
        nodo_min_distancia = min(
            (nodo for nodo in grafo.nodes if nodo not in visitados),
            key=lambda nodo: distancia[nodo]
        )
        visitados.add(nodo_min_distancia)

        
        for vecino, peso in grafo[nodo_min_distancia].items():
            nueva_distancia = distancia[nodo_min_distancia] + peso['weight']
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                predecesores[vecino] = nodo_min_distancia

    return distancia, predecesores

def obtener_nodos_camino_mas_corto(predecesores, nodo_origen, nodo_destino):
    
    nodo_actual = nodo_destino
    nodos_camino = [nodo_actual]
    while nodo_actual != nodo_origen:
        nodo_actual = predecesores[nodo_actual]
        nodos_camino.append(nodo_actual)
    nodos_camino.reverse()
    return nodos_camino

def main():
    # Crear el grafo y añadir los nodos y aristas
    G = nx.Graph()

    # Colocar los nodos y sus posiciones
    nodos = range(1, 42)
    posiciones = {
        1: (1, 6), 2: (3, 6), 3: (4, 6), 4: (5, 6), 5: (7, 6), 6: (9, 6), 7: (10, 6), 
        8: (7, 5), 9: (8, 5), 10: (9, 5), 
        11: (1, 4), 12: (2, 4), 13: (4, 4), 14: (6, 4), 15: (7, 4), 16: (8, 4), 17: (9, 4), 18: (10, 4),
        19: (2,3), 20: (3, 3), 21: (4, 3), 22: (5, 3), 23: (6, 3), 24: (8, 3), 25: (9, 3), 26: (10, 3),
        27: (1, 2), 28: (2, 2), 29: (3, 2), 30: (5, 2), 31: (6, 2), 32: (7, 2), 33: (8, 2), 34: (9, 2),
        35: (1, 1), 36: (3, 1), 37: (4, 1), 38: (5,1), 39: (7, 1), 40: (9, 1), 41: (10, 1),
    }
    G.add_nodes_from(nodos)
    nx.set_node_attributes(G, posiciones, 'pos')

    # Colocar las aristas y sus valores
    aristas = [
        (1, 2, {'weight': 20}), (1, 11, {'weight': 30}),
        (2, 3, {'weight': 10}),
        (3, 4, {'weight': 10}), (3, 13, {'weight': 30}),
        (4, 5, {'weight': 20}),
        (5, 6, {'weight': 20}), (5, 8, {'weight': 10}),
        (6, 7, {'weight': 10}), (6, 10, {'weight': 10}),
        (7, 18, {'weight': 35}),
        (8, 9, {'weight': 10}), (8, 15, {'weight': 20}),
        (9, 10, {'weight': 10}), (9, 16, {'weight': 20}),
        (10, 17, {'weight': 20}),
        (11, 12, {'weight': 10}), (11, 27, {'weight': 20}),
        (12, 13, {'weight': 20}), (12, 19, {'weight': 10}),
        (13, 14, {'weight': 20}), (13, 21, {'weight': 10}),
        (14, 15, {'weight': 10}), (14, 23, {'weight': 10}),
        (15, 16, {'weight': 10}), (15, 32, {'weight': 20}),
        (16, 17, {'weight': 10}), (16, 24, {'weight': 10}),
        (17, 18, {'weight': 10}), (17, 25, {'weight': 10}),
        (18, 26, {'weight': 10}),
        (19, 20, {'weight': 10}), (19, 28, {'weight': 10}),
        (20, 21, {'weight': 10}), (20, 29, {'weight': 10}),
        (21, 22, {'weight': 10}), (21, 37, {'weight': 20}),
        (22, 23, {'weight': 10}), (22, 30, {'weight': 10}),
        (23, 31, {'weight': 10}),
        (24, 25, {'weight': 10}), (24, 33, {'weight': 10}),
        (25, 26, {'weight': 10}), (25, 34, {'weight': 10}),
        (26, 41, {'weight': 20}),
        (27, 28, {'weight': 10}), (27, 35, {'weight': 10}),
        (28, 29, {'weight': 10}),
        (29, 36, {'weight': 10}), 
        (30, 31, {'weight': 10}), (30, 38, {'weight': 15}),
        (31, 32, {'weight': 10}),
        (32, 33, {'weight': 10}), (32, 39, {'weight': 15}),
        (33, 34, {'weight': 10}),
        (34, 40, {'weight': 15}),
        (35, 36, {'weight': 20}),
        (36, 37, {'weight': 10}),
        (37, 38, {'weight': 10}),
        (38, 39, {'weight': 20}),
        (39, 40, {'weight': 20}),
        (40, 41, {'weight': 10})
    ]
    G.add_edges_from(aristas)

    # Solicitar al usuario que ingrese los nodos de origen y destino
    while True:
        try:
            source_node = int(input("Ingrese el nodo de origen (1-41): "))
            destination_node = int(input("Ingrese el nodo de destino (1-41): "))
            if source_node in G.nodes and destination_node in G.nodes:
                break
            else:
                print("Nodos inválidos. Por favor, ingrese nodos válidos del 1 al 41.")
        except ValueError:
            print("Por favor, ingrese valores numéricos.")

    # Calcular el camino más corto desde el nodo de origen al nodo de destino
    shortest_distances, predecessors = metodo_dijkstra(G, source_node)
    shortest_distance = shortest_distances[destination_node]

    # Obtener los nodos que forman parte del camino más corto
    path_nodes = obtener_nodos_camino_mas_corto(predecessors, source_node, destination_node)

    # Imprimir el resultado
    print(f"El camino más corto desde el nodo {source_node} al nodo {destination_node} es {shortest_distance}")
    print(f"El camino pasa por los siguientes nodos: {path_nodes}")

    # Graficar el grafo
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos=posiciones, with_labels=True, node_size=1000, node_color='skyblue')
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos=posiciones, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos=posiciones, edgelist=[(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)], edge_color='red', width=2)
    plt.title("Grafo con el algoritmo de Dijkstra")
    plt.show()

if __name__ == "__main__":
    main()
