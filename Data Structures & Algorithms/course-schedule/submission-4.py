class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        visited = set()
        path = set()
        def dfs(course):
            visited.add(course)
            path.add(course)

            for neighbour in graph[course]:
                if neighbour in path:
                    return False

                if neighbour not in visited:
                    if not dfs(neighbour):
                        return False
            path.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        return True
        