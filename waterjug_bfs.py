from collections import deque
import math

def is_goal_state(jug1, jug2, goal):
    return jug1 == goal or jug2 == goal

def water_jug_bfs(capacity1, capacity2, goal):
    visited = set()
    queue = deque([(0, 0)])  
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        if is_goal_state(jug1, jug2, goal):
            print(f"Goal reached: Jug1 = {jug1}, Jug2 = {jug2}")
            return
        
        visited.add((jug1, jug2))
        
   
        possible_states = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)), 
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))  
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
    
    print("No solution found")

def main():
    capacity1 = int(input("Enter the capacity of the first jug: "))
    capacity2 = int(input("Enter the capacity of the second jug: "))
    goal = int(input("Enter the goal amount of water: "))

    if goal > max(capacity1, capacity2):
        print("Goal amount is greater than the capacity of both jugs. No solution possible.")
        return
    
    if goal % math.gcd(capacity1, capacity2) != 0:
        print("No solution possible: GCD of the capacities does not divide the goal amount.")
        return
    
    water_jug_bfs(capacity1, capacity2, goal)

if __name__ == "__main__":
    main()
