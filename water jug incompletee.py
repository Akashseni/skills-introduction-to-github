def WaterJugDFS(jug1, jug2, target):
    visited = set()
    path = []

    def dfs(a,b):
        if (a, b) in visited:
            return False
        #if not visited ass the state to the visited
        visited.add((a,b))
        path.append((a,b))
        #check if target has reached
        if a == target or b == target:
            return True
        #fill jug1
        if dfs(jug1, b):
            return True
        #fill jug2
        if dfs(a, jug2):
            return True
        #empty first jug
        if dfs(0, b):
            return True
        #empty second jug
        if dfs(a, 0):
            return True
        #pour water from first jug to second jug
        if dfs(max(0, a-(jug2-b)), min(jug2, a+b)):
            return True
        #pour water from left jug to right jug
        if dfs(min(jug1, a+b), max(0, b-(jug1-a)):
               return True

        
