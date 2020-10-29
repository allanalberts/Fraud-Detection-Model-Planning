# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical to a merchants success. Fraud detection models are used to classifiy transactions as either legitimate or suspected fraud. The merchant must then decide whether to spend resources manually verifying fraud on the suspect transactions or simply automatically declining them. Auto declining incorrectly will result in lost revenue and customer alienation. Therefore, it is critical to have a model with high degree of accuracy in detecting high dollar fraud, but also maintain enough precision to not overwhelm the manual review resources with false positives. This project will provide insight into the difference in potential effectiveness from utilizing a single fraud prediction model vs two models segmented on transaction amount. 

The dataset used in the project contains transactions made by credit cards in September 2013 by european cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. 

The potential model effectiveness will be compared by independently evaluating the 28 fraud detection features and determine which ones best distinguish fraud and non-fraud transactions when transactions are segmented by amount vs. viewed as a single population. 

![](/img/overview.png) 
### Types of Fraud

![](img/AmountPlot.png)
3.5x greater and 52x greater than the average


- describe why peak dollar amounts are occurring (rule based and testing). 
### Hypothesis:
The Hypothesis that we will be exploring is if there is evidence that there will be a difference in fraud detection performance from two models built on different features and utilizing data from different transaction groups (over a dollar vs equal to or lower than a dollar). This hypthosesis will be initially validated by estimating differences in feature importance based on the p-value obtained from independently comparing the fraud to non-fraud transactions for each feature. 


### Feature Importance:
Feature importance is estimated based on a lack of similarity between the distributions of the fraud and non-fraud samples. A low p-value will indicate that the distributions are very different for the specific feature and therefore a model utilizing this feature will have a good likelihood of correctly classifying the transactions as fraud vs. non-fraud.

< insert visual>

- summary - in addition to detecting differently, may want different thesholds on the precision recall curve for tolerance lower accuracy tolerance at low dollar amounts (losses not as high and manual labor is a limited resource)




