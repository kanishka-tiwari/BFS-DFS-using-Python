#Input a simple dictionary graph directly

raw_input = input("Enter graph dictionary (example: {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}): ")
graph = eval(raw_input)  

start_node = input("Enter starting node: ")
algorithm = input("Choose (BFS / DFS): ").strip().upper()
