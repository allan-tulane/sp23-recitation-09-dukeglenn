from collections import deque
from heapq import heappush, heappop 
import heapq

def shortest_shortest_path(graph, source):
    dist = {v: (float('inf'), float('inf')) for v in graph}
    dist[source] = (0, 0)
    pq = [(0, source, 0)]
    explored = set()
    while pq:
        d, u, n = heapq.heappop(pq)
        if u in explored:
            continue
        explored.add(u)
        for v, w in graph[u]:
            new_dist = dist[u][0] + w
            new_num_edges = dist[u][1] + 1
            if new_dist < dist[v][0] or (new_dist == dist[v][0] and new_num_edges < dist[v][1]):
                dist[v] = (new_dist, new_num_edges)
                heapq.heappush(pq, (new_dist, v, new_num_edges))
    return dist
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
  parent = {v: None for v in graph}
  parent[source] = source
  q = deque([source])
  while q:
    u = q.popleft()
    for v in graph[u]:
      if parent[v] is None:
        parent[v] = u
        q.append(v)
  return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
  path = []
  while destination != parents[destination]:
    path.append(destination)
    destination = parents[destination]
  path.reverse()
  return path

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
