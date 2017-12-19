'''
Created on 22 Nov. 2017

@author: Alvin UTS
'''

from sklearn.manifold import TSNE

def DimReduction (data):
    data_embedded = TSNE(n_components=2, early_exaggeration=12, learning_rate=200, n_iter_without_progress=300).fit_transform(data)
    print ('Dimension Reduction Done', '\n')
    return data_embedded