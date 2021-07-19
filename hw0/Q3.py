import numpy as np
import snap
import matplotlib.pyplot as plt

PATH = 'stackoverflow-Java.txt'

# load the data as a directed graph
G1 = snap.LoadEdgeList(snap.TNGraph, PATH, 0,1)

print(len(G1.GetWccs()))
# 10143 weakly connected components

largest_wcc = G1.GetMxWcc()
print(len(list(largest_wcc.Nodes())))
print(len(list(largest_wcc.Edges())))
# 131188 nodes and 322486 edges are contained in the largest wcc

page_rank = G1.GetPageRank()
node_centrality = []
node_id = []
for i in page_rank:
    node_id.append(i)
    node_centrality.append(page_rank[i])

for itr in range(3):
    idx = np.argmax(node_centrality)
    print(node_id[idx], end=' ')
    del node_centrality[idx]

# node ids are 992484, 135152, 22656

node_id = []
hubs = []
authorities = []
hub_hits, authorities_hits = G1.GetHits()
for i in hub_hits:
    node_id.append(i)
    hubs.append(hub_hits[i])

idxs = np.argsort(hubs)[::-1]
for i in range(3):
    print(node_id[idxs[i]], end=' ')

# id of top3 hubs are 892029 1194415 359862

node_id = []
for i in authorities_hits:
    node_id.append(i)
    authorities.append(authorities_hits[i])

idx = np.argsort(authorities)[::-1]
for itr in range(3):
    print(node_id[idx[itr]], end=' ')
# id of top3 authorities are 22656 157882 571407