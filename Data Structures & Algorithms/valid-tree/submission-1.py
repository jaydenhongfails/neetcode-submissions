class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(node, parent):
            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
            
                if neighbor in visit:
                    return False

                if not dfs(neighbor,node):
                    return False
            return True
        
        valid = dfs(0,-1)

        return valid and len(visit) == n
        