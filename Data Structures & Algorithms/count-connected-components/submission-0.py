class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)
                
        components = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                components += 1
        return components