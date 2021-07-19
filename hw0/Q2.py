import numpy as np
import snap
import matplotlib.pyplot as plt

PATH = 'Wiki-Vote.txt'

# load the data as a directed graph
G1 = snap.LoadEdgeList(snap.TNGraph, PATH, 0,1)

# snap.PlotOutDegDistr(G1, "Wiki-Vote", "Wiki-Vote Out Degree")
# this line cannot be run unless you have installed gnuplot

# plot the distribution of out-degrees of nodes
DegToCntV = snap.TIntPrV()
G1.GetOutDegCnt(DegToCntV)# returns (out-degree, # of nodes)
out_degree = []
num_nodes = []
for item in DegToCntV:
    out_degree.append(item.GetVal1())
    num_nodes.append(item.GetVal2())

plt.plot(out_degree,num_nodes)
plt.xscale("log")
plt.yscale("log")
# plt.show()

# out_degree = np.array(out_degree)
# num_nodes = np.array(num_nodes)

for idx in range(len(out_degree)):
    if num_nodes[idx] == 0:
        del num_nodes[idx]
        del out_degree[idx]
del num_nodes[0]
del out_degree[0]
log_out_degree = np.log10(out_degree)
log_num_nodes = np.log10(num_nodes)
ls_param = np.polyfit(log_out_degree, log_num_nodes, deg=1)

x = np.linspace(out_degree[0],out_degree[-1])
y = np.power(10,ls_param[1])*np.power(x,ls_param[0])
plt.plot(x,y,color = 'red')
plt.show()