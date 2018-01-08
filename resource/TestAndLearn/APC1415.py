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



def process_file(f):
    #diag_dict = pd.read_csv(os.path.join(settings.BASE_DIR, 'data/D_ICD_DIAGNOSES.csv'))
    #doc = pd.read_csv(f)
    #new_doc = doc[new_features]
    rawdata = pd.read_csv(f, dtype= str)
    #distinct_dias = new_doc.DIAGNOSES_CODE.unique()
    #distinct_pates = new_doc.PATIENT_ID.unique()
    df = rawdata.drop([0])
    df["1"] = df["1"].astype(int)
    distinct_pates = df['1'].unique()
    
    DDXlist = [ ]
    DDXvalue = ""
    
    for idno in distinct_pates:
        dfDDXbyID = df[df["1"] == idno].iloc[:,95:195]
        dfIni = dfDDXbyID['95']
        for col in range (96, 195):
            dfFin = pd.concat([dfIni,dfDDXbyID[str(col)]])
            dfIni = dfFin
        ''' concat col by col'''
        diglist = dfFin.dropna().tolist()
        
        value = ','.join([str(code) for code in diglist])
        #print ("value", value)
        DDXvalue = DDXvalue + value + ","
        '''DDXvalue is a long string including all DDX'''
        #print ("DDXvalue", DDXvalue)
        DDXlist.append(diglist)
  
        
    
    DDXvalueSeparate = [x for x in DDXvalue.split(",") if x is not '']
    DDXsetUnique = set(DDXvalueSeparate)
    DDXlistUnique = list(DDXsetUnique) 
    print ("DDXlistUnique", "\n", DDXlistUnique)
    '''1d list to store all distinct DDX'''
    #distinct_dias = np.asarray(DDXlistUnique)
    #distinct_pates = IDarr
    
    dfDDX = pd.DataFrame(DDXlist)
    #print (dfDDX.head(50))

    #diag_dict = pd.read_csv('data/D_ICD_DIAGNOSES.csv')
    #doc = pd.read_csv(f)
    #new_doc = doc[new_features]

    diags_desc = []
    data = []  
    
    for i in range (0, len(distinct_pates)):
        #print p
        vec = np.zeros(len(DDXlistUnique),dtype=int)
        #ps = new_doc[new_doc['PATIENT_ID']==p]
        #print ps.DIAGNOSES_CODE
        str_diags_codes = '\t'.join([str(code) for code in dfDDX.loc[i].dropna().tolist()])
        
        #print str_diags_codes
        #descs = []
        #print ("i",i)
        #print ("dfDDX.loc[i].dropna().tolist()", dfDDX.loc[i].dropna().tolist())
        for code in dfDDX.loc[i].dropna().tolist():

            #print ("code", code)
            index = DDXlistUnique.index(code)
            #print ("index", index)
            vec[index] += 1
            #desc = diag_dict[diag_dict['ICD9_CODE']==code].SHORT_TITLE
            #if (not desc.empty):
                #descs.append(desc.iloc[0])
            
        #str_diags_desc = '\t'.join(descs )
        diags_desc.append(str_diags_codes)
        #print vec.shape
        data.append(vec)
        #diags.append(str_diags_codes)
    
    sparse_data = sparse.csr_matrix(data)
    print ('data', '\n', data)
    print ('sparse_data', '\n', sparse_data)
    
    num_topics = 10
    
    mdl = topic(sparse_data, num_topics)
    mdl2 = topic(data, num_topics)
    print ("mdl", "\n", mdl,"\n", len(mdl))
    print ("mdl2", "\n", mdl2,"\n", len(mdl2))
    cols = ['topic_{}'.format(i) for i in range(len(mdl[0]))]
    #df_reperent = pd.DataFrame(mdl, columns=cols)
    #print ("df_reperent", "\n", df_reperent,"\n", len(df_reperent))


if __name__ == "__main__":
    process_file ("C://Users//Alvin UTS//Desktop//DoH Linked Data//Sample Data//0910//Test_Alvin_50.csv")