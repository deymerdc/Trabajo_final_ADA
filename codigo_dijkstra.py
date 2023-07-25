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