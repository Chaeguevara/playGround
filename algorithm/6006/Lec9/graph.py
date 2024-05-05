def bfs(Adj:list,s):
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while 0 <len(level[-1]):
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    print(level)
    return parent

test_graph = [
    [1,2,3],
    [0],
    [0],
    [0]
]

def unweighted_shortest_path(Adj, s, t):
    parent = bfs(Adj,s)
    if parent[t] is None:
        return None
    i= t
    path  = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1]