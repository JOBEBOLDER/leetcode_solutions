#bfs is the best way to find the shorest pathfrom collections import defaultdict, deque
from typing import List
'''	•	总复杂度：O(n * k)'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Step 1: build graph: stop -> set of bus routes
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        # Step 2: initialize BFS
        seen_stop = set([source])
        seen_route = set()
        q = deque([source])
        ans = 0  # number of buses taken

        # Step 3: BFS traversal
        while q:
            for _ in range(len(q)):
                stop = q.popleft()

                # If we reach the target stop
                if stop == target:
                    return ans

                # All bus routes that pass through this stop
                for routeId in graph[stop]:
                    if routeId not in seen_route:
                        seen_route.add(routeId)  # mark this route as used
                        for new_stop in routes[routeId]:
                            if new_stop not in seen_stop:
                                seen_stop.add(new_stop)
                                q.append(new_stop)

            ans += 1  # after exploring all current stops, we increase bus count

        return -1