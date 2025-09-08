#Experiment - 7

import heapq

# Define goal state for 8-puzzle
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the moves (Up, Down, Left, Right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

# Manhattan Distance Heuristic Function
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:  # Skip the empty space
            goal_pos = GOAL_STATE.index(state[i])
            distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

# Function to check if a given state is the goal state
def is_goal_state(state):
    return state == GOAL_STATE

# Function to generate possible moves
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)  # Find the position of the empty space (0)
    zero_row, zero_col = zero_pos // 3, zero_pos % 3

    for move in MOVES:
        new_row, new_col = zero_row + move[0], zero_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:  # Valid move
            new_pos = new_row * 3 + new_col
            # Create new state by swapping the empty space with the new position
            new_state = state[:]
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(new_state)
    
    return neighbors

# A* Search to solve the 8-puzzle
def a_star_search(initial_state):
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(initial_state), 0, initial_state, []))  # (f, g, state, path)
    visited = set()
    visited.add(tuple(initial_state))

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)

        if is_goal_state(current_state):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                h = manhattan_distance(neighbor)
                heapq.heappush(open_list, (g + 1 + h, g + 1, neighbor, path + [current_state]))

    return None

# Function to display the puzzle grid
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

# Interactive User Input
def main():
    print("Enter the initial state of the 8-puzzle (use 0 for the empty space):")
    initial_state = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} (3 numbers, space-separated): ").split()))
        initial_state.extend(row)
    
    if sorted(initial_state) != list(range(9)):
        print("Invalid input! The puzzle must contain numbers from 0 to 8.")
        return
    
    print("Initial State:")
    print_puzzle(initial_state)

    solution = a_star_search(initial_state)
    
    if solution:
        print("\nSolution Found:")
        for step in solution:
            print_puzzle(step)
            print("")
    else:
        print("No solution found!")

if __name__ == "__main__":
    main()
