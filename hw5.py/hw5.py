def is_there_cycle(g):
    n<-len(g)
    taken<-[]
    for i in range(n):
        taken.append(False) 

    for v from 0 to n-1:
        if taken[v] =false:
            if dfs(v, parent = -1):
                return true
            
    return False

def dfs(node,parent,taken,g):
    taken[node]<-true 
    for each neigh in g[node]:
        if taken[neigh] = false:
            if dfs(neigh, node) = true:
                return true
        else if neigh != parent:
            return true

    return false


