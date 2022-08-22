# importing libraries

import pandas as pd
import networkx as nx
import random 
import matplotlib.pyplot as plt
from sklearn import metrics

# Reading data from the csv file
df=pd.read_csv('data/1994-2022.csv', sep=";")
print(df.head())


# Drawing network
Graphtype = nx.complete_graph(len(df))
G = nx.from_pandas_edgelist(df, source='player_1name', target='player_2name', create_using=Graphtype)
pos= nx.spring_layout(G)
d = dict(G.degree)
node_size = [d[v] for v in G.nodes()]
plt.figure(figsize=(20, 10))
nx.draw(G,pos,node_color='#5F9EA0',edge_color='#ADD8E6', node_size=node_size, with_labels=False)
plt.show()

# Network configuration

n = G.number_of_nodes()
m = G.number_of_edges()

proportion_edges = 0.2
edge_subset = random.sample(G.edges(), int(proportion_edges * G.number_of_edges()))

# Create a copy of the graph and remove the edges
G_train = G.copy()
G_train.remove_edges_from(edge_subset)

# plt.figure(figsize=(1,8))
# nx.draw(G_train)
# plt.gca().collections[0].set_edgecolor("#000000") # set node border color to black

edge_subset_size = len(list(edge_subset))
print("Number of edges deleted : %d" % edge_subset_size)
print("Number of edges remaining : %d" % (m - edge_subset_size))


# Make prediction using Common Neighbor
pred_cn = list(nx.common_neighbor_centrality(G_train))
score_cn, label_cn = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_cn])

# Compute the ROC AUC Score
fpr_cn, tpr_cn, _ = metrics.roc_curve(label_cn, score_cn)
auc_cn = metrics.roc_auc_score(label_cn, score_cn)
print("Common Neighbor", auc_cn)

plt.plot(fpr_cn, tpr_cn)
plt.title('Common Neighbor')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()

# Make prediction using Jaccard Coefficient
pred_jaccard = list(nx.jaccard_coefficient(G_train))
score_jaccard, label_jaccard = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_jaccard])

# Compute the ROC AUC Score
fpr_jaccard, tpr_jaccard, _ = metrics.roc_curve(label_jaccard, score_jaccard)
auc_jaccard = metrics.roc_auc_score(label_jaccard, score_jaccard)
print("Jaccard Coefficient : ", auc_jaccard)

plt.plot(fpr_jaccard, tpr_jaccard)
plt.title('Jaccard Coefficient')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()

# Make prediction using Adamic Adar
pred_adamic = list(nx.adamic_adar_index(G_train))
score_adamic, label_adamic = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_adamic])

# Compute the ROC AUC Score
fpr_adamic, tpr_adamic, _ = metrics.roc_curve(label_adamic, score_adamic)
auc_adamic = metrics.roc_auc_score(label_adamic, score_adamic)
print("Adamic-Adar : ", auc_adamic)

plt.plot(fpr_adamic, tpr_adamic)
plt.title('Adamic-Adar')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()

# Make prediction using Resource Allocation
pred_ra = list(nx.resource_allocation_index(G_train))
score_ra, label_ra = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_ra])

# Compute the ROC AUC Score
fpr_ra, tpr_ra, _ = metrics.roc_curve(label_ra, score_ra)
auc_ra = metrics.roc_auc_score(label_ra, score_ra)
print("Resource Allocation: ", auc_ra)

plt.plot(fpr_ra, tpr_ra)
plt.title('Resource Allocation')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()

# Make prediction using Preferential Attachment
pred_pa = list(nx.preferential_attachment(G_train))
score_pa, label_pa = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_pa])

# Compute the ROC AUC Score
fpr_pa, tpr_pa, _ = metrics.roc_curve(label_pa, score_pa)
auc_pa = metrics.roc_auc_score(label_pa, score_pa)
print("Preferential Attachment : ", auc_pa)

plt.plot(fpr_pa, tpr_pa)
plt.title('Preferential Attachment')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()

# Make prediction using Sorensen Coefficient
pred_sorensen = list(nx.sorensen_coefficient(G_train))
score_sorensen, label_sorensen = zip(*[(s, (u, v) in edge_subset) for (u, v, s) in pred_sorensen])

# Compute the ROC AUC Score
fpr_sorensen, tpr_sorensen, _ = metrics.roc_curve(label_sorensen, score_sorensen)
auc_sorensen = metrics.roc_auc_score(label_sorensen, score_sorensen)
print("Sorensen Coefficient : ", auc_sorensen)

plt.plot(fpr_sorensen, tpr_sorensen)
plt.title('Sorensen Coefficient')
plt.ylabel('TPR')
plt.xlabel('FPR')
plt.show()