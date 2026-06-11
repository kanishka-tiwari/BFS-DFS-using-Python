#Depth first search (uses recursion)

elif algorithm == "DFS":
    visited = []

    def run_dfs(node):
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                run_dfs(neighbor)

    run_dfs(start_node)
    print(f"DFS Traversal Order: {visited}")