# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical to a merchants success. Fraud detection models are used to classifiy transactions as either legitimate or suspected fraud. The merchant must then decide whether to spend resources manually verifying fraud on the suspect transactions or automatically declining them. Auto declining incorrectly will result in lost revenue and customer alienation. Therefore, it is critical to have a model with high degree of accuracy in detecting high dollar fraud, but also maintain enough precision to not overwhelm the manual review resources with false positives. 

The goal of this project is to provide insight into the benefits of developing a fraud detection strategy based on using a single predictive model or two models segmented on low vs. high transaction amounts. This insight will come from identifying transaction features that would likely be good predictors of fraud for each of these segments. 


## The Dataset
The dataset used in the project contains transactions made by credit cards in September 2013 by European cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced with the positive class (frauds) accounting for 0.172% of all transactions. 

![](/img/overview.png) 

The dataset comes courtesy of Kaggle and has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group (http://mlg.ulb.ac.be) of ULB (Université Libre de Bruxelles) on big data mining and fraud detection.


## Inspecting the Fraud
The data set contains fraud transaction ranging in value from $0 to over $2000. However, almost 80% of the fraud transactions are under $100  representing approximately 15% of the overall fraud dollars (green area of chart on left). 

![](/img/AmountPlots.png)

Looking closer at the fraud transactions that under $100, we see two anomalous spikes (green chart on right).

There are an excessive amount of fraud transactions occurring at $99.99. In fact, there are 58 times as many fraud purchases as legitimate purchases at this price point. This anomaly is indicative of a merchant that uses a rule based fraud detection system instead of a machine learning model. The fraudsters have figured out that the merchant reviews transactions at a $100 of more, so they attempt fraudulent purchases just under this threshold. 

The other anomaly occurs at $1 and below. There are 3.5 times more fraud than non-fraud transactions in this price range. Fraud done at very low dollar amounts serves a different purpose than fraud that is being directly monetized. Fraudsters use these low transaction amounts to test accounts to see if they have already been closed. They will then use the active accounts to make a higher value purchase. 

This project will test the potential improvement in fraud detection by creating two predictive models. One based on transactions that are at or below $1 and the other based on transactions above $1. 

## Fraud Features
The dataset also includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. The impact of these features on model effectiveness will be measured by independently evaluating each one to determine how well they distinguish distributions of fraud and non-fraud transactions. 

The hypothesis is that low and high transaction amount models will perform better individually as each represents a different type of fraud that may be represented differently by the fraud detection features.

## Identifying Relevant Fraud Detection Features
Feature importance will be estimated based on a lack of similarity between the distributions of the fraud and non-fraud samples as determined from an independent t-test for each feature. A low p-value will indicate that the distributions are very different for the specific feature and therefore a model utilizing this feature will have a good likelihood of correctly classifying transactionss as fraud vs. non-fraud.


## Results:

![](/img/features_pval.png)

Using an extremely low p-value threshold of 0.001 for identifying featurees that may be highly relevant to fraud prediction, I found that both the low and high dollar models share the following predictive features:  
 
V1, V2, V3, V4, V5, V6, V7, V9, V10, V11, V12, V14, V16, V17, V18, V20

The low amount model will benefit from the addition features V15, V24, V26.

The high amount model will benefit from the addition features V8, V19, V21. 

Raising the p-value threshold to 0.01 results in 2 addition features added to the low model: V13 and V28.

## Conclusion
I found that multiple predictive models would likely produce better overall fraud identification based on usage of features that are relevant for each tranaction amount segment. If further analysis is desired, one could also compare the differences in the standard deviation and median values between non-fraud transaction and a bootstrap of the fraud transactions.


