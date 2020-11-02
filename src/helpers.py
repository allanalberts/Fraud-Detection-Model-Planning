import scipy.stats as stats
import pandas as pd
import numpy as np

def load_data(datafile):
    """
    Returns an pandas dataframe containg the source data and a list containg the fraud features to be analyzed.

    Parameters
    ----------
    datafile: csv file containg transaction dataset to be analyzed

    Returns
    -------
    data - Pandas Dataframe
    Features - list
    """
    data = pd.read_csv("../data/creditcard.csv")
    Features = ['V%d' % n for n in range(1, 29)]
    return data, Features


def bootstrap_mean(df, statistic, samples=500):
    """
    Returns an pandas series of mean bootstrap values for the statistic
    for each of the columns in the dataframe.

    Parameters
    ----------
    df: Pandas dataframe
    statistic: valid arguments include 'mean', 'median', 'std'
    samples: number of bootstrap samples to generate

    Returns
    -------
    Pandas Series
    """

    df_bootstrap = pd.DataFrame(columns=df.columns)
    for _ in range(samples):
        bootstrap = df.sample(n=len(df), replace=True, axis=0)
        if statistic == 'mean':
            df_bootstrap = df_bootstrap.append(bootstrap.mean(), ignore_index=True)
        elif statistic == 'median':
            df_bootstrap = df_bootstrap.append(bootstrap.median(), ignore_index=True)
        elif statistic == 'std':
            df_bootstrap = df_bootstrap.append(bootstrap.std(), ignore_index=True)
        else:
            print("Invalid statitic. Please use 'mean', 'median' or 'sdt'")
            return None
    return df_bootstrap.mean()



def ttest(sample1, sample2, Features):
    """
    Returns a dataframe with a single row containing the p values for each Feature when sample1
    is compared against sample2. Features are columns in the dataframe.

    Parameters
    ----------
    sample1: Pandas dataframe represting the sample transactions and their associated features.
    sample2: Pandas dataframe represting the sample transactions and their associated features.
    Features: List of column names from input dataframes that are to be evaluated.

    Returns
    -------
    Pandas DataFrame
    """

    p_lst = []
    for f in Features:
        stat, p_val = stats.ttest_ind(sample1[f], sample2[f], equal_var=False)  
        p_lst.append(p_val)
    df = pd.DataFrame(p_lst, index=Features).reset_index()
    df.columns = ['Feature','p_val']
    return df

def print_fraud_rate(TranAmt, data, cummulative=False):
    '''
        Prints the fraud rates for specific price points
        
        ARGS:
            TranAmt -> dollar value to rate analysis
            data -> pandas df
            cummulative - boolean value if rate should include all values below TranAmt
           
        Return:
            None
    '''    

    if TranAmt == 0:
        print(f"Overall Fraud rate: {100 * data['Class'].mean():0.2f}%")
    else:
        if cummulative:
            print(f"<=${TranAmt:0.2f} Fraud rate: {100 * data[data['Amount']<=TranAmt]['Class'].mean():0.2f}%")
        else:
            print(f"${TranAmt:0.2f} Fraud rate: {100 * data[data['Amount']==TranAmt]['Class'].mean():0.2f}%")
    return None


def relevant_features(fraud_sample, legit_sample, Features, p_threshold):
    '''
        Creates a list of relevant features based on p-value vs p-threshold
        
        ARGS:
            fraud_sample - pandas dataframe of fraud transactions to analyze
            legit_sample - pandas dataframe of non-fraud transactions to analyze
            Features - list of features to analyze
            p_threshold - number to compare p-value against
            
        Return:
            list of features
    '''
    low_p_features = []
    for f in Features:
        stat, p_val = stats.ttest_ind(fraud_sample[f], legit_sample[f], equal_var=False) 
        if p_val < p_threshold:
            low_p_features.append(f)
    return low_p_features

def print_recommended_features(data, Features, amt_threshold, p_threshold):
    '''
        Prints a list of relevant features for fraud models
        
        ARGS:
            data - pandas dataframe containing dataset to be analyzed
            Features - list of features
            amt_threshold - dollar amount used to segment the data for analysis
            p_threshold - number used to specify p-value limit for identifying relevant features

        Return:
            None
    '''
    fraud_sample_low = data[(data['Class']==1) & (data['Amount']<=amt_threshold)]
    legit_sample_low = data[(data['Class']==0) & (data['Amount']<=amt_threshold)]
    fraud_sample_high = data[(data['Class']==1) & (data['Amount']>amt_threshold)]
    legit_sample_high = data[(data['Class']==0) & (data['Amount']>amt_threshold)]
    

    low_amt_f = relevant_features(fraud_sample_low, legit_sample_low, Features, p_threshold)
    high_amt_f = relevant_features(fraud_sample_high, legit_sample_high, Features, p_threshold)
    
    both = [x for x in low_amt_f if x in high_amt_f]
    low_only = [x for x in low_amt_f if x not in high_amt_f]
    high_only = [x for x in high_amt_f if x not in low_amt_f]                    
                        
    print(f'Relevenant Features for Both models: \r\n{both}')
    print(f'\nAdditional Features for Low Amount model only: {low_only}')
    print(f'\nAdditional Features for High Amount model only: {high_only}')
    return None

if __name__ == '__main__':
    data, Features = load_data("../data/creditcard.csv")

    print_fraud_rate(0, data)
    print_fraud_rate(99.99, data)
    print_fraud_rate(1.00, data)
    print_fraud_rate(1.00, data, cummulative=True)

    print_recommended_features(data, Features, amt_threshold=1.00, p_threshold=0.01)    
