# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical for merchant success. A fraud detection model is created to classifiy transactions as either legitimate or suspected fraud. The merchant must then decide whether to spend resources manually verifying fraud on the suspect transactions or simply automatically declining them. Auto declining incorrectly will result in lost revenue and customer alienation. Therefore, it is critical to have a model with high degree of accuracy in detecting high dollar fraud, but also maintain enough precision to not overwhelm the manual review resources with false positives. This project will provide insight into the difference in potential effectiveness from utilizing a single fraud prediction model vs two models segmented on transaction amount. 

The dataset used in the project contains transactions made by credit cards in September 2013 by european cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. 

The potential model effectiveness will be compared by independently evaluating the 28 fraud detection features and determine which ones best distinguish fraud and non-fraud transactions when transactions are segmented by amount vs. viewed as a single population. 

### Fraud vs. Non-Fraud

![](..\img\overview.png) 

- insert chart showing cdf of fraud and non fraud by price point.
- insert chart showing peak dollar amounts 
- describe why peak dollar amounts are occurring (rule based and testing). 
- Hypothesis that testing is a different from of fraud and may be detected differently

- test if fraud segments are different

- summary - in addition to detecting differently, may want different thesholds on the precision recall curve for tolerance lower accuracy tolerance at low dollar amounts (losses not as high and manual labor is a limited resource)




