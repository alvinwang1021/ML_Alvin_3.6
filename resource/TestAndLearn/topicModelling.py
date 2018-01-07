'''
Created on 3 Jan. 2018

@author: Alvin UTS
'''

import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.decomposition import LatentDirichletAllocation

def topic(df, num_topics=5):
    """
    Represent the topics features of original features
    :param df: pandas DataFrame
    :param num_topics: the number of topics, default=5
    :return: the probability vectors of each topics the entry belongs to
    """

    lda = LatentDirichletAllocation(n_topics=num_topics,
                                    max_iter=5,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
    return lda.fit_transform(df)



num_topics = 3


data = [[0.1,0,0.35,0,0,0,0,0,0,10],[0.5,0,0.33,0,0.33,1,0,0,0,15],[0.2,1,0,0.33,0,0.25,0,0,0,8],[0,1,0,0.5,0,0.25,0,0,0,20]]

mdl = topic(data, num_topics)
#mdl2 = topic(data, num_topics)
print ("mdl", "\n", mdl,"\n", len(mdl))
#print ("mdl2", "\n", mdl2,"\n", len(mdl2))
#cols = ['topic_{}'.format(i) for i in range(len(mdl[0]))]
#df_reperent = pd.DataFrame(mdl, columns=cols)
#print ("df_reperent", "\n", df_reperent,"\n", len(df_reperent))


    