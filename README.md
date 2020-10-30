# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical to a merchants success. Fraud detection models are used to classifiy transactions as either legitimate or suspected fraud. The merchant must then decide whether to spend resources manually verifying fraud on the suspect transactions or automatically declining them. Auto declining incorrectly will result in lost revenue and customer alienation. Therefore, it is critical to have a model with high degree of accuracy in detecting high dollar fraud, but also maintain enough precision to not overwhelm the manual review resources with false positives. 

The goal of this project is to provide insight into the benefits of developing a fraud detection strategy based on using a single predictive model or two models segmented on low vs. high transaction amounts. This insight will come from identifying transaction features that would likely be good predictors of fraud for each of these segments. 

### The Dataset
The dataset used in the project contains transactions made by credit cards in September 2013 by European cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced with the positive class (frauds) accounting for 0.172% of all transactions. 

![](/img/overview.png) 

### Inspecting the Fraud
The data set contains from fraud transaction ranging in value from \\$0 to over \\$2000. However, almost 80% of the fraud transactions are under $100  representing approximately 15% of the overall fraud dollars (green area of chart). 

![](/img/AmountPlots.png)

Looking closer at the fraud transactions that under \\$100, we see two anomalous spikes (green chart).

There are an excessive amount of fraud transactions occurring at //$99.99. In fact there are 58 times as many fraud purchases as legitimate purchases at this price point. This anomaly is indicative of a merchant that uses a rule based fraud detection system instead of a machine learning model. The fraudsters have figured out that the merchant reviews transactions at a $100 of more, so make fraudulent purchases just under this threshold. 

The other anomoaly occurs at //$1 and below. There are 3.5 times more fraud than non-fraud transactions at this price range. Fraud done for very low dollar amounts serves a different purpose than fraud that is being directly monetized. Fraudsters use these low transaction amounts to test accounts to see if they have already been closed. They will then use the good accounts to make a higher value purchase. 

# Fraud Features
The dataset also includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. The impact of these features on model effectiveness will be measured by independently evaluating each one to determine how well they distinguish distributions of fraud and non-fraud transactions. 

- maybe show multiple hist plots of the features???

### Identifying Relevant Fraud Detection Features
Feature importance will be estimated based on a lack of similarity between the distributions of the fraud and non-fraud samples as determined from an independent t-test for each feature. A low p-value will indicate that the distributions are very different for the specific feature and therefore a model utilizing this feature will have a good likelihood of correctly classifying the transactions as fraud vs. non-fraud.

![] image of features for all transactions

### Results:

Using a p-value threshold of 0.01 for identifying featurees that may be highly relevant to fraud prediction, I found that both the low and high dollar models share the following predictive features:


The low value model will benefit from the addition features VVVVVV and VVVVVV.


The low value model will benefit from the addition features VVVVVV and VVVVVV.


### Conclusion
I found that multiple predictive models would likely produce better overall fraud identification based on usage of features that are relevant for each tranaction amount segment. Further analysis can be also be undertaken by comparing the differences in the standard deviation and median values between non-fraud transaction and a bootstrap of the fraud transactions.

In addition to performance difference, a multi-model approach to fraud management can have additional benefits from having the ability to select a different precision-recall threshold for low vs higher dollar transactions. For lower dollar transactions, a merchant may benefit from using a lower recall and higher precision model to automatically deny suspect fraud without manual review. The lower recall would allow more fraud to occur but the losses would be relative small due to the transaction amount and the higher precision would reduce customer alienation.
