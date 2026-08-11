class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        state = [0] * numCourses

        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1: # cycle
                return False
            
            state[course] = 1
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False # cycle

            state[course] = 2
            # at this point all the future 
            # courses completable by the
            # prereq is done.
            order.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order