"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
"""
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if not routes or len(routes)==0:
            return -1

        if S==T:
            return 0

        n = len(routes)
        stops = collections.defaultdict(list)
        for bus in range(n):
            for s in routes[bus]:
                stops[s].append(bus)

        # bfs
        q = [S]
        dist = dict()
        dist[S] = 0
        bustaken = set()

        while q:
            s = q.pop(0)
            d = dist[s] + 1
            for bus in stops[s]:
                if bus not in bustaken:
                    bustaken.add(bus)
                    for stop in routes[bus]:
                        if stop == T:
                            return d
                        if stop not in dist:
                            dist[stop] = d
                            q.append(stop)

        return -1