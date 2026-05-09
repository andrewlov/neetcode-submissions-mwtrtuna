class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses) }
        for course, pre in prerequisites:
            prereq[course].append(pre)
        visit, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output