#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


 
def all(a):
    print("1.density","2.degreeofeachnode","3.centrality","4.closeness_centrality ","5.closeness_centrality_sorted ","6.betweenness_centrality","7.betweenness_centrality_sorted","8.gatekeepers","9.graphconnectedornot","10.nodes in largest connected component","11.densityof largest connected subgraph","12.diameter of graph connected components","13.total cliques","14.cliques","15.largest clique","16.size of largest clique","17.ego_network","18.graph",sep='\n')     
    c=int(input("what do you calculate from graph? : "))
    if c == 1:
        
        density(a)        
    elif c == 2:       
        
        degreeofeachnode(a)

    elif c == 3:
        
        centrality(a)           

    elif c == 4:
        
        closeness_centrality(a)

    elif c == 5:
        
        closeness_centrality_sorted(a)
          
    elif c==6:
        
        betweenness_centrality(a)
          
    elif c==7:
        
        betweenness_centrality_sorted(a)
    elif c==8:
        
        gatekeepers(a)
    elif c==9:
        graphconnectedornot(a)
          
    elif c==10:
        
        nodesinlcc(a)
          
    elif c==11:
        
        densityoflcsb(a)
          
    elif c==12:
        
        diameterofgcc(a)
          
    elif c==13:
        
        totalcliques(a)
          
    elif c==14:
        
        cliques(a)
          
    elif c==15:
        
        largestclique(a)
          
    elif c==16:
        
        sizeoflargestclique(a)
          
    elif c==17:
        
        ego_network(a)

    elif c==18:
        
        
        graph(a)       

    else:
        
        print("wrong input entered")










def density(a):
    print((nx.density(a)))

def degreeofeachnode(a):
    print((sorted((d, n) for n, d in a.degree())))

def centrality(a):
  in_dc = nx.degree_centrality(a)
  in_dc_sorted = {k: v for k, v in sorted(
  in_dc.items(),
  key=lambda item: item[1],
  reverse=True
  )}
  l=in_dc_sorted.items()
  l2=list(l)[:10]
  for k,v in l:

    print (f'{k} -> {v:.3f}')
    


def closeness_centrality(a):
  l5 = nx.closeness_centrality(a).items()
  l6=list(l5)[:10]

  for k,v in l5:
    print (f'{k} -> {v:.3f}')

# closeness_centrality(facebook)

def closeness_centrality_sorted(a):
  closeness = nx.closeness_centrality(a)
  c_sorted = {k: v for k, v in sorted(
    closeness.items(),
    key=lambda item: item[1],
    reverse=True
  )}
  l7=c_sorted.items()
  l8=list(l7)[:10]
  for k,v in l7:
    print (f'{k} -> {v:.3f}')

# closeness_centrality_sorted(facebook)

def betweenness_centrality(a):
  l9 = nx.betweenness_centrality(a).items()
  l10 = list(l9)

  for k,v in l10:
    print (f'{k} -> {v:.3f}')

# betweenness_centrality(facebook)

def betweenness_centrality_sorted(a):
    
    
    between = nx.betweenness_centrality(a)
    b_sorted = {k: v for k, v in sorted(
    between.items(),
    key=lambda item: item[1],
    reverse=True
  )}
    

    l11 = b_sorted.items()
    l12 =list(l11)
    
    for k,v in l12:
        print (f'{k} -> {v:.3f}')

# betweenness_centrality_sorted(facebook)

def gatekeepers(a):
    gK = sorted(nx.betweenness_centrality(a).items(), key = lambda x : x[1],  reverse=True)
    

    for i in gK:
        
        print(i)

# gatekeepers(facebook)

def graphconnectedornot(a):
  print('The graph {} connected.'.format('is' if nx.is_connected(a) else 'is not'))
  print('Number of connected components:', nx.number_connected_components(a))

# graphconnectedornot(facebook)

def nodesinlcc(a):
  largest = max(nx.connected_components(a), key=len)
  print(len(largest))

# nodesinlcc(facebook)


def densityoflcsb(a):
  largest = max(nx.connected_components(a), key=len)

  large = a.subgraph(largest)
  print(nx.density(large))

# densityoflcsb(facebook)


def diameterofgcc(a):
  b=int(input("enter component of grapg :"))
  cc = list(nx.connected_components(a))
  cc1 = facebook.subgraph(cc[b])
  print("Component 1:", list(cc1.nodes))
  diameter_1 = nx.diameter(cc1)
  apl_1 = nx.average_shortest_path_length(cc1)
  print("diameter:", diameter_1)
  print("average path length: {:.2f}".format(apl_1))

  print('')

# diameterofgcc(facebook,0)

def totalcliques(a):
  from networkx.algorithms import approximation, clique
  n_of_cliques = clique.graph_number_of_cliques(a)
  print("Number of cliques in the network:", n_of_cliques)

# totalcliques(facebook)

def cliques(a):
  from networkx.algorithms import approximation, clique
  cliques = clique.find_cliques(a)
  for i in cliques:
    print(i)

# cliques(facebook)

def largestclique(a):
  from networkx.algorithms import approximation, clique
  largest = approximation.clique.max_clique(a)
  print( largest)


# largestclique(a)

def sizeoflargestclique(a):
    
    from networkx.algorithms import approximation, clique

    largestcliquesize = clique.graph_clique_number(a)
    print( largestcliquesize)

# sizeoflargestclique(facebook)

def ego_network(a):
  b=int(input("enter node of graph :"))
  ego_network = nx.ego_graph(a, b)
  nx.draw(ego_network)

# ego_network(facebook)


def graph(a):
  ego = cores[0][0]
  gk_ego = nx.ego_graph(a, ego)
  pos = nx.spring_layout(gk_ego)
  nx.draw(gk_ego, pos, node_color='black', node_size=100, with_labels=False)
  nx.draw_networkx_nodes(gk_ego, pos, nodelist=[ego], node_size=100, node_color='purple')
  plt.show()

# graph(facebook)


# In[ ]:





# In[5]:





# In[6]:





# In[ ]:





# In[ ]:





# In[1]:





# In[ ]:





# In[ ]:




