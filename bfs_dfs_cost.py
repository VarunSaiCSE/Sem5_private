from collections import deque
import heapq

# Unweighted graph for BFS and DFS
unweighted_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Weighted graph for UCS
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))
    return None

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                stack.append((neighbor, path + [neighbor]))
    return None

def ucs_shortest_path(graph, start, goal):
    heap = [(0, start, [start])]
    visited = {}
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path, cost
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

def main():
    print("Available nodes:", list(unweighted_graph.keys()))
    start = input("Enter the START node: ").strip().upper()
    goal = input("Enter the GOAL node: ").strip().upper()

    if start not in unweighted_graph or goal not in unweighted_graph:
        print("Invalid node(s). Please enter nodes from:", list(unweighted_graph.keys()))
        return

    print("\n--- Shortest Path Results ---")

    bfs_result = bfs_shortest_path(unweighted_graph, start, goal)
    if bfs_result:
        print(f"BFS Path (unweighted): {bfs_result}")
    else:
        print("No BFS path found.")

    dfs_result = dfs_path(unweighted_graph, start, goal)
    if dfs_result:
        print(f"DFS Path (unweighted): {dfs_result}")
    else:
        print("No DFS path found.")

    ucs_result, ucs_cost = ucs_shortest_path(weighted_graph, start, goal)
    if ucs_result:
        print(f"UCS Path (weighted): {ucs_result}, Cost: {ucs_cost}")
    else:
        print("No UCS path found.")

if __name__ == "__main__":
    main()
