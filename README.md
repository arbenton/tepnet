## tepnet

A simulation of disease dispersion over historic trade networks.

#### The Data

The trade network is constructed from the [Old World Trade Routes Project](http://www.ciolek.com/owtrad.html), 
by Dr. T. Matthew Ciolek of Australian National University. 

Dr. Ciolek is pretty thorough about stating the efficacy of each route, but for my purposes, I'm assuming that
if it is on there, it is a valid trade route. 

#### The Math

The workhorse of this program is a simple loop that expresses a recursive function describing the transfer of
disease over the network.

```python
for i in range(epochs):
    pulse = np.tanh(pulse * transm)
```

In this function, `transm` is a matrix which expresses the transmission of the disease per epoch. It is a
summation of the adjacency matrix of the trade network and the identity matrix (both with scaling).

```python
transm = r*nx.adjacency_matrix(graph) + m*sp.eye(nx.number_of_nodes(graph))
```

The `pulse` array begins as all zeros, with element set to a small value. This represents the proportion of
infection in the network.

#### Some Nifty Graphs

The system generally levels out into steady state behavior. For example, this time series shows a circumstance 
where the disease was able to "get a footing". In this case, it levels out. This is by far the most common case
that is actually interesting.

![time series](https://github.com/arbenton/tepnet/blob/master/time_series.png)

More excitingly, if the disease is able to spread, it will infect an entire subgraph. This network graph
corresponds to the above parameters.

![network graph](https://github.com/arbenton/tepnet/blob/master/network.png)

Finally, there's some amazing dynamic behavior in the early epochs.

![dynamic](https://github.com/arbenton/tepnet/blob/master/zoom.png)

