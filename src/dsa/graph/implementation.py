class AdjacencyList:
    def __init__(self, vertex_count: int) -> None:
        self.vertexes = []
        for i in range(vertex_count):
            linked = [int(v) for v in input(f"Vertexes linked to v{i}: ").split(",")]
            self.vertexes.append(linked)

    def __str__(self) -> str:
        s = "Graph - Adjacency list representation\n"
        for i, v in enumerate(self.vertexes):
            s += f"{i}: {v} \n"
        return s


vertex_count = int(input("Enter the count of vertex: "))
graph = AdjacencyList(vertex_count)
print(graph)
