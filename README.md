# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical to a merchants success. Fraud detection models are used to classifiy transactions as either legitimate or suspected fraud. The merchant must then decide whether to spend resources manually verifying fraud on the suspect transactions or automatically declining them. Auto declining incorrectly will result in lost revenue and customer alienation. Therefore, it is critical to have a model with high degree of accuracy in detecting high dollar fraud, but also maintain enough precision to not overwhelm the manual review resources with false positives. This project will provide insight into the difference in potential effectiveness from utilizing a single fraud prediction model vs two models segmented on transaction amount. 

### The Dataset
The dataset used in the project contains transactions made by credit cards in September 2013 by European cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. 

The potential model effectiveness will be compared by independently evaluating the 28 fraud detection features and determine which ones best distinguish fraud and non-fraud transactions when transactions are segmented by amount vs. viewed as a single population. 

![](/img/overview.png) 

### Inspecting the Fraud
The data set contains from fraud transaction ranging in value from \\$0 to over \\$2000. However, almost 80% of the fraud transactions are under $100 (green area of chart) representing approximately 15% of the overall fraud dollars. Looking closer at the fraud transactions that under //$100, we see two anomalous spikes (green chart). 

There is an excessive amount of fraud transactions occurring at //$99.99. In fact there are 58 times as many fraud purchases as legitimate purchases at this price point. This anomaly is indicative of a merchant that uses a rule based fraud detection system instead of a machine learning model. The fraudsters have figured out that the merchant reviews transactions at a $100 of more, so make fraudulent purchases just under this threshold. 

The other anomoaly occurs at //$1 and below. There are 3.5 times more fraud than non-fraud transactions at this price range. Fraud done for very low dollar amounts serves a different purpose than fraud that is being directly monetized. Fraudsters use these low transaction amounts to test accounts to see if they have already been closed. They will then use the good accounts to make a higher value purchase. 

### Identifying Relevant Fraud Detection Features
In this project, we will estimate the varying level of effectiveness each of the 28 transaction features may have on a fraud prediction model. This will be achieved by comparing, independently for each feature, the fraud transaction distribution with that of the non-fraud transactions using a t-test. A very low p-value will indicate that the two distributions are not similar and thus the feature will likely be effective at predicting fraud.

![] image of features for all transactions

When we run the population as a whole and compare fraud with non fraud distributions, we can see that 20 of the 28 features will likely be most effective predicters.

### Hypothesis

Since fraud at or below //$1 is a fundamentally different type of fraudulent use, I hypothesis that low dollar fraud samples will have improved detection with a model that utilized different fraud detection features than a model optimized for high value fraud detection. I will evaluate my hypothesis by comparing each of the 28 fraud detection features against low and high value transtions and identify if the features vary in fraud to non-fraud population similarity for the two groups.

have different fraud detection features 

examine if these transactions differ from the distribution of fraud sampled from higher price points when compared with the distribution of legitate sales in the price ranges.

We will explore each fraud detection feature and measure the similarty between fraud and non fraud for the two transaction amount segments.

it's similarity to  Specifically we will perform t-test on each individual fraud feature to see the level of similarity between the distributions of low and high dollar fraud. A low p-value would indicate that the populations are highly dissimilar and therefore 




In order to manage this fraud, a merchant is going to want their fraud detection engine to have a high degreee of accuracy for identifying the small subset of fraud which is at higher transaction amounts. Likely, they will likely be auto-denying suspected fraud for the high volume of frauds at low price points.

![](/img/AmountPlots.png)

#### Add Text here  
- 3.5x greater and 52x greater than the average
- describe why peak dollar amounts are occurring (rule based and testing). 

### Hypothesis:
The Hypothesis being exploring is that there is evidence that difference likely exist in fraud detection performance from using a single predictive model compared with using two models built on different features that also use data from different transaction groups (over a dollar vs equal to or lower than a dollar). This hypthosesis will be initially validated by estimating differences in feature importance based on the p-value obtained from independently comparing the fraud to non-fraud transactions for each feature. The hypothesis can ultimately be tested by building and testing three diffenent preditive models.



### Feature Importance:
Feature importance is estimated based on a lack of similarity between the distributions of the fraud and non-fraud samples. A low p-value will indicate that the distributions are very different for the specific feature and therefore a model utilizing this feature will have a good likelihood of correctly classifying the transactions as fraud vs. non-fraud. ure

#### insert plot here
The analysis shows that X of features (list them) are too similar between the fraud and non-fraud classes. These features should be avoided in a machine learning model as they may contribute negatively and lead to overfitting and false positives. 

### Addition Reasons for Multi-Model approach
In addition to performance difference, a multi-model approach to fraud management can have additional benefits from having the ability to select a different precision-recall threshold
for low vs higher dollar transactions. 

or lower dollar transactions, a merchant may benefit from using a lower recall and higher precision model to automatically deny suspect fraud without manual review. The lower recall would allow more fraud to occur but the losses would be relative small due to the transaction amount. The higher precision would reduce customer alienation.

#### insert plot here

Where to go from here? where do you make the split between models??


### Conclusing
summary - in addition to detecting differently, may want different thesholds on the precision recall curve for tolerance lower accuracy tolerance at low dollar amounts (losses not as high and manual labor is a limited resource)

