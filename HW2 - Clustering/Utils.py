import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

def get_updated_data(f_name: object, l_non_numeric_cols: list ) -> [pd.core.frame.DataFrame,pd.core.frame.DataFrame]:
    df = pd.read_csv('college_data.csv')
    df_labels = df[l_non_numeric_cols].copy()
    df.drop((['Unnamed: 0'] + l_non_numeric_cols),axis=1,inplace=True)
    return df, df_labels

def scale_data(df: pd.core.frame.DataFrame, scaler: StandardScaler) -> pd.core.frame.DataFrame:
    array_scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(array_scaled, columns=list(df.columns))
    return df_scaled

def show_num_elbow_clusters(df: pd.core.frame.DataFrame, model: KMeans, o_metric_to_use: object):
    visualizer = KElbowVisualizer(model, k=(2,20), metric = o_metric_to_use, timings=False)
    visualizer.fit(df)        
    visualizer.show()        

def find_k_means_clusters (df: pd.core.frame.DataFrame,df_labels: pd.core.frame.DataFrame,
                   k_means_model: KMeans,scaler: StandardScaler) -> pd.core.frame.DataFrame:
    k_means_model.fit(df)
    clusters = k_means_model.predict(df)
    centers = k_means_model.cluster_centers_
    array_unscaled = scaler.inverse_transform(df)    
    df_coll_unscaled = pd.DataFrame(array_unscaled, columns=list(df.columns))
    df_coll_unscaled['Clusters'] = clusters
    df_coll_unscaled_clustered = pd.merge(df_coll_unscaled,df_labels,on=df.index)
    return df_coll_unscaled_clustered        

def remove_non_float_dtypes(df: pd.core.frame.DataFrame, df_dict: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    print('Original Shape:', df.shape,'\n')
    print('Original data type distribution:\n',df_dict['API data type'].value_counts())
    float_cols = list(df_dict[df_dict['API data type'] == 'float']['VARIABLE NAME'])
    float_cols = list(np.setdiff1d(float_cols,['C200_L4_POOLED_SUPP', 'C200_4_POOLED_SUPP', 'C150_L4_POOLED_SUPP', 'C150_4_POOLED_SUPP']))
    iden_cols = list(df.columns[0:4])
    iden_cols.append('PREDDEG')
    float_cols = iden_cols + float_cols
    df_updated = df[float_cols]
    print('\nUpdated Shape:', df_updated.shape)
    return df_updated

def remove_data_elements_with_greater_than_10pct_nan(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    floats_cols_low_nans = list(((df.isna().sum())/len(df))[((df.isna().sum())/len(df)) < .1].index)
    df = df[floats_cols_low_nans]
    df = df[floats_cols_low_nans].dropna()
    print('Updated Shape:', df.shape)
    return df
   

def remove_certificate_assoc_degree_schools(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    print('All Schools:',df.shape[0])
    df = df[(df.PREDDEG >= 2)]
    print('Schools Bestowing Bachelors or higher:',df.shape)
    return df

def remove_Priv_Supp(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    o_PS = 'PrivacySuppressed' 
    grt15pct_PS_cols = list(((df.astype(str) == o_PS).sum()/
                         len(df))[((df.astype(str) == o_PS).sum()/
                         len(df))>.1].index)
    df =  df[list(np.setdiff1d(df.columns,grt15pct_PS_cols))]
    df =  df[np.setdiff1d(df.columns,['DEP_STAT_PCT_IND'])].copy()
    df.drop(df[(df.astype(str) == o_PS).any(axis=1)].index,inplace=True)
    return(df)

def convert_object_to_float(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    l_cols_to_convert_to_floats = list(df.dtypes[df.dtypes == 'object'].index)
    l_cols_to_convert_to_floats.remove('INSTNM')
    df[l_cols_to_convert_to_floats] = df[l_cols_to_convert_to_floats].astype(float)
    return df

def create_new_features(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    l_type_of_degree_cols = ['PCIP01', 'PCIP03', 'PCIP04', 'PCIP05', 'PCIP09', 'PCIP10', 'PCIP11',
       'PCIP12', 'PCIP13', 'PCIP14', 'PCIP15', 'PCIP16', 'PCIP19', 'PCIP22',
       'PCIP23', 'PCIP24', 'PCIP25', 'PCIP26', 'PCIP27', 'PCIP29', 'PCIP30',
       'PCIP31', 'PCIP38', 'PCIP39', 'PCIP40', 'PCIP41', 'PCIP42', 'PCIP43',
       'PCIP44', 'PCIP45', 'PCIP46', 'PCIP47', 'PCIP48', 'PCIP49', 'PCIP50',
       'PCIP51', 'PCIP52', 'PCIP54']
    for col in ['PAR_ED_PCT_1STGEN','CDR3','APPL_SCH_PCT_GE2']:
        new_cols = [x+y for x, y in zip(l_type_of_degree_cols , ([col]*len(l_type_of_degree_cols)))]
        df[new_cols] = df[l_type_of_degree_cols].multiply(df[col],axis='index')
    return df