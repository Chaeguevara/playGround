def bfs(Adj:list,s):
    """Get parent of each vertex toward 's' direction

    Args:
        Adj (list): Adjacency list. Each index corresponds to the vertex key. Item is Adjacent vertices array
        s (_type_): Vertex

    Returns:
        parent(list): Parent of each vertex. From itself to 's'
    """
    parent = [None for _ in Adj] #Initialize parent array
    parent[s] = s # parent of start is start itself
    level = [[s]] # the first level is itself then distance 1 levelset => distance 2 level set => ...
    while 0 <len(level[-1]): # O(?)
        print(f"{parent=}")
        level.append([]) #O_a(1)
        for u in level[-2]: #O(?)
            for v in Adj[u]: #O(Adj[u])
                if parent[v] is None: #O(1)
                    parent[v] = u # O(1)
                    level[-1].append(v) #O_a(1)
    print(level)
    return parent

test_graph = [
    [1,4,3],
    [0],
    [3],
    [0,2],
    [0]
]
print(bfs(test_graph,0))

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