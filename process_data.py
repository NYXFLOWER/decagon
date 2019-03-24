import csv
import numpy as np
import scipy.sparse as sp

# def drug_drug_adj_list(size):

dic = {}
adj = []
with open("data_decagon/bio-decagon-combo.csv", 'r') as f:
    ppi = csv.reader(f)
    next(ppi)
    for line in ppi:
        i = int(line[2].split('C')[-1])
        r = int(line[0].split('D')[-1])
        c = int(line[1].split('D')[-1])
        if not dic.get(i):
            dic[i] = [], []
        else:
            dic[i][0].append(r)
            dic[i][1].append(c)
    for i in dic.keys():
        adj.append(sp.csr_matrix(([1] * len(dic[i][0]), (dic[i][0], dic[i][1]))))

#     [col, row] = list(zip(*gene_drug))
#     col = [int(c.split('D')[-1]) for c in col]
#     row = [int(r) for r in row]
# gene_drug_adj = csr_matrix([1]*len(row), (list(row), list(col)))
