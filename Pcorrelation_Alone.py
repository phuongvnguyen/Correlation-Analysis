#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Pcorrelation(data,threshold,figsizes):
    """
    data:
    threshold: 0.4
    figsizes: (15, 10)
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # compute Pearson correlations
    correlation = data.corr()
    
    # Showing correlation matrix 
    plt.figure(figsize=figsizes)
    mask1 = np.zeros_like(correlation, dtype=np.bool)
    mask1[np.triu_indices_from(mask1)] = True
    cmap = 'Dark2'# sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation,cmap=cmap, mask=mask1,annot=True,
            square=True
           ,vmax=.3, center=0,
            linewidths=.5, cbar_kws={"shrink": 0.7})
    plt.title('The Correlation Of Two Attributes',fontsize=15, fontweight='bold')
    sns.set(font_scale=1)
    
    
    # picking up the upper triangle of the correlation matrix
    correlation_up=correlation.where(np.triu(np.ones(correlation.shape), k = 1).astype(np.bool))
    # selecting the attribute
    select_corr= [column for column in correlation_up.columns if any(abs(correlation_up[column])>threshold)]
    # printing
    print('------------------------------------------------------------------')
    print('This program was developed by Phuong Van Nguyen')
    print('------------------------------------------------------------------')
    print('The number of the attributes has the higher-threshold correlation: {}'.
         format(len(select_corr)))
    print('------------------------------------------------------------------')
    print('The list of the attributes has the higher-threshold correlation:')
    print(select_corr)
    print('------------------------------------------------------------------')
    # recording the result
    ## creating a dataframe with three columns to record the result.
    record_select_correlation=pd.DataFrame(columns=['Attribute_1','Attribute_2','Correlation_Value'])
    ## doing record
    for column in select_corr:
        # Finding the first attributes wih the higher-threshold correlation
        Attribute_11=list(correlation_up.index[abs(correlation_up[column])>threshold])
        # Finding its counterpart attribute
        Attribute_21=[column for _ in range(len(Attribute_11))]
        # Fulfilling the correlation values
        Correlation_Value1=list(correlation_up[column][abs(correlation_up[column])>threshold])
        # Recording them into a temporary data framework
        temp_df_corr=pd.DataFrame.from_dict({'Attribute_1': Attribute_11,
                                      'Attribute_2': Attribute_21,
                                      'Correlation_Value': Correlation_Value1})
        # Adding temp_df to the created dataframe
        record_select_correlation=record_select_correlation.append(temp_df_corr,ignore_index=True)
    print('-------------------------------------------------------------')
    print('Recording the higher-threshold correlations:')
    print('-------------------------------------------------------------')
    print(record_select_correlation)
    print('------------------------------The End-----------------------')
    return record_select_correlation;

