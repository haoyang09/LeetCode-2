import collections

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations or not values:
            return []
        
        G = collections.defaultdict(dict)
        for eq, val in zip(equations, values):
            a, b = eq
            G[a][b] = val*1.0
            G[b][a] = 1.0/val
            
        res = []
        for a,b in queries:
            if a not in G or b not in G:
                res.append(-1.0)
            elif a==b:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(G, a, b, visited))
                
        return res
                
                
def dfs(G, a, b, visited):
    print(a,b)
    visited.add(a)
    for ap in G[a]:
        if ap not in visited:
            if ap == b:
                return G[a][ap]
            
            temp = dfs(G, ap, b, visited)
            if temp!=-1.0:
                return G[a][ap] * temp
            visited.remove(ap)
    return -1.0

equations = [ ["a","b"],["b","c"] ]
values = [2.0,3.0]
queries = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
s = Solution()
res = s.calcEquation(equations, values, queries)
print(res)


equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
s = Solution()
res = s.calcEquation(equations, values, queries)
print(res)