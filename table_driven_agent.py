#Experiment - 4.2

A = 'A'
B = 'B'

# Accumulated percept history
percepts = []
# Table mapping sequences of percepts to actions
table = {
    ((A, 'clean'),): 'right',
    ((A, 'dirty'),): 'suck',
    ((B, 'clean'),): 'left',
    ((B, 'dirty'),): 'suck',
    ((A, 'dirty'), (A, 'clean')): 'right',
    ((A, 'clean'), (A, 'clean')): 'right',
    ((A, 'clean'), (A, 'dirty')): 'suck',
    ((A, 'dirty'), (A, 'clean'), (B, 'dirty')): 'suck',
    ((A, 'clean'), (A, 'clean'), (A, 'clean')): 'right'
}

def lookup(percepts, table):
    """Look up an action based on full percept history."""
    action = table.get(tuple(percepts))
    print("Lookup for", tuple(percepts), "=>", action)
    return action

def tabledrivenagent(percept):
    global percepts
    percepts.append(percept)
    return lookup(percepts, table)

def run():
    print("Action \t\t Percepts")
    print(tabledrivenagent((A, 'dirty')), '\t', percepts)
    print(tabledrivenagent((A, 'clean')), '\t', percepts)
    print(tabledrivenagent((B, 'dirty')), '\t', percepts)

run()
