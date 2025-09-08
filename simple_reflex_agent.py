#Experiment - 4.1

# Initial state of rooms
rooms = {
    'A': 'Dirty',
    'B': 'Dirty',
    'C': 'Dirty',
    'D': 'Dirty'
}

# Order in which the agent moves
room_order = ['A', 'B', 'C', 'D']

# Initial agent location
agent_location = 'A'

# Reflex rules for action based on percepts
rules = {
    ('A', 'Dirty'): 'Suck',
    ('B', 'Dirty'): 'Suck',
    ('C', 'Dirty'): 'Suck',
    ('D', 'Dirty'): 'Suck',
    ('A', 'Clean'): 'MoveNext',
    ('B', 'Clean'): 'MoveNext',
    ('C', 'Clean'): 'MoveNext',
    ('D', 'Clean'): 'MoveNext'
}

def get_percept():
    return agent_location, rooms[agent_location]

def interpret_input(percept):
    location, status = percept
    return (location, status)

def rule_match(interpreted_input):
    return rules.get(interpreted_input, 'NoOp')  # Default fallback

def status():
    print(f"Agent is in room {agent_location} | Room status: {rooms}")

def execute_action(action):
    global agent_location
    if action == 'Suck':
        rooms[agent_location] = 'Clean'
        print(f"Action: Cleaned room {agent_location}")
    elif action == 'MoveNext':
        current_index = room_order.index(agent_location)
        next_index = (current_index + 1) % len(room_order)
        agent_location = room_order[next_index]
        print(f"Action: Moved to room {agent_location}")
    else:
        print("Action: No operation (NoOp)")

# Run the agent for 10 steps
for step in range(10):
    print(f"\nStep {step + 1}")
    percept = get_percept()
    interpreted_input = interpret_input(percept)
    action = rule_match(interpreted_input)
    status()
    execute_action(action)
