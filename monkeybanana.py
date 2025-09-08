#Experiment - 3

from collections import deque

# Define all locations in the room.
locations = ['A', 'B', 'C']

# Define the goal state: Monkey and box are at 'C', monkey is on the box, and has the banana.
GOAL = ('C', 'C', True, True)

def get_possible_actions(state):
    monkey, box, on_box, has_banana = state
    actions = []
    

    if has_banana:
        return []

    for loc in locations:
        if loc != monkey:
            actions.append(('walk', loc))

    if monkey == box and not on_box:
        for loc in locations:
            if loc != monkey:
                actions.append(('push', loc))

    if monkey == box:
        if not on_box:
            actions.append(('climb_up',))
        else:
            actions.append(('climb_down',))

    if monkey == 'C' and box == 'C' and on_box:
        actions.append(('grab',))

    return actions

def apply_action(state, action):
    monkey, box, on_box, has_banana = state
    action_type = action[0]

    if action_type == 'walk':
        return (action[1], box, False, has_banana)
    elif action_type == 'push':
        return (action[1], action[1], False, has_banana)
    elif action_type == 'climb_up':
        return (monkey, box, True, has_banana)
    elif action_type == 'climb_down':
        return (monkey, box, False, has_banana)
    elif action_type == 'grab':
        return (monkey, box, on_box, True)

    return state

def solve(start_state):
    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL:
            return path + [('Goal Reached!',)]

        for action in get_possible_actions(current_state):
            new_state = apply_action(current_state, action)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))
    
    return None

def get_user_input():
    print("Enter initial positions for Monkey and Box (choose from A, B, C):")
    while True:
        monkey = input("Monkey Position: ").strip().upper()
        if monkey in locations:
            break
        print("Invalid input. Please enter A, B, or C.")
    
    while True:
        box = input("Box Position: ").strip().upper()
        if box in locations:
            break
        print("Invalid input. Please enter A, B, or C.")

    while True:
        on_box_input = input("Is Monkey on the box? (yes/no): ").strip().lower()
        if on_box_input in ['yes', 'no']:
            on_box = on_box_input == 'yes'
            break
        print("Invalid input. Please enter yes or no.")

    # Initial state: (monkey_pos, box_pos, on_box, has_banana=False)
    return (monkey, box, on_box, False)

# Main execution
if __name__ == "__main__":
    start_state = get_user_input()
    print(f"\nSolving from initial state: {start_state}\n")
    solution = solve(start_state)

    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")
