class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # not possible only when cycle
        visited = [0] * numCourses
        # we convert to a dict for fast access
        adjlist = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
        
        def dfs(course):
            if visited[course] == 1: # current
                return True # cycle detected

            if visited[course] == 2: 
                # visited in the past
                return False

            visited[course] = 1 # current path
            for next_course in adjlist[course]:
                if dfs(next_course): #if cycle
                    return True # propogate cycle
            
            visited[course] = 2 # none in its path
            return False # this path seems fine
        
        for course in range(numCourses):
            if visited[course] == 0 and dfs(course):
                return False
        
        return True
