#Breadth first search (uses queue)

if algorithm == "BFS":
    visited = [start_node]
    queue = [start_node]
    
    while queue:
        current = queue.pop(0)  
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor) 
                
    print(f"BFS Traversal Order: {visited}")