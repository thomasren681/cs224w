import snap

PATH = 'Wiki-Vote.txt'

# load the data as a directed graph
G1 = snap.LoadEdgeList(snap.TNGraph, PATH, 0,1)

# number of nodes in the graph
print(len(list(G1.Nodes())))
# 7115 nodes in the graph
# for node in G1.Nodes():
#     print(node.GetId())

print(G1.CntSelfEdges())
# no self edges in the graph

print(G1.CntUniqDirEdges())
# 103689 unique directed edges

print(G1.CntUniqUndirEdges())
# 100762 unique undirected edges

print(G1.CntUniqBiDirEdges())
# 2927 reciprocated edges

print(G1.CntOutDegNodes(0))
# 1005 nodes have zero out-degree

print(G1.CntInDegNodes(0))
# 4734 nodes have zero in-degree

num_outdeg = 0
num_indeg = 0
for node in G1.Nodes():
    if node.GetOutDeg() > 10:
        num_outdeg += 1
    if node.GetInDeg() < 10:
        num_indeg += 1

print(num_outdeg)
# 1612 nodes have out-degree more than 10
print(num_indeg)
# 5165 nodes have in-degree less than 10