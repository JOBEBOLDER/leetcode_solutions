'''You are given N tasks, labeled 0 … N-1.
Each task i has:

a priority p[i] (smaller = higher priority)

a duration t[i]

zero or more dependencies (a DAG):
u → v meaning task u must finish before v starts

You also have K workers, each capable of working on at most one task at a time.

A task becomes available when all its dependencies are completed.

Your goal is to compute the minimum total completion time to finish all tasks under the following scheduling rule:

Among all currently available tasks, workers must take the ones with the highest priority first. If multiple tasks have equal priority, choose a smaller task id first. Workers can start tasks as soon as they become available. If the dependency graph contains a cycle → return -1.
'''




from heapq import heappush, heappop
from typing import List, Tuple

def min_total_completion_time(
    n: int,
    p: List[int],                 # priority, smaller = higher
    t: List[int],                 # duration
    deps: List[Tuple[int, int]],  # edges u -> v
    k: int                        # number of workers
) -> int:
    if n == 0:
        return 0
    if k <= 0:
        return -1  # no workers but tasks exist

    # Build graph + indegree
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in deps:
        g[u].append(v)
        indeg[v] += 1

    # available tasks: (priority, task_id)
    available = []
    for i in range(n):
        if indeg[i] == 0:
            heappush(available, (p[i], i))

    # running tasks: (finish_time, priority, task_id)
    running = []

    time = 0
    free_workers = k
    done = 0

    while done < n:
        # Assign tasks as long as we have free workers and available tasks
        while free_workers > 0 and available:
            pri, task_id = heappop(available)
            finish = time + t[task_id]
            heappush(running, (finish, pri, task_id))
            free_workers -= 1

        # If nothing is running but we still have unfinished tasks -> cycle (or deadlock)
        if not running:
            return -1

        # Advance time to next completion event
        next_finish = running[0][0]
        time = next_finish

        # Pop all tasks that finish at this time
        finished_now = []
        while running and running[0][0] == time:
            _, pri, task_id = heappop(running)
            finished_now.append(task_id)
            free_workers += 1
            done += 1

        # Update indegrees, unlock new available tasks
        for u in finished_now:
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heappush(available, (p[v], v))

    return time


# --------- Example usage ----------
if __name__ == "__main__":
    n = 5
    p = [1, 0, 2, 0, 1]             # smaller is higher
    t = [3, 2, 4, 1, 2]
    deps = [(1, 2), (0, 2), (3, 4)] # u -> v
    k = 2
    print(min_total_completion_time(n, p, t, deps, k))

