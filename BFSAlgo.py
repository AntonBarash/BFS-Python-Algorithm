import sys
from queue import *
#test
def  BFS(N, s, adj_list):

    level = ['x']*N
    discovered = [False]*N
    Q = Queue()
    for source in s:
        Q.put(source)
        level[source] = 0
        discovered[source] = True
    while Q.empty() == False:
        node = Q.get()
        for neighbor in adj_list[node]:
            if discovered[neighbor] == False:
                discovered[neighbor] = True
                Q.put(neighbor)
                level[neighbor] = level[node] + 1
    return level
