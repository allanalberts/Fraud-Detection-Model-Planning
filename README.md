# Fraud Detection Model Planning

Managing the costs associated with credit card fraud is critical for merchant success. A balance must be maintained between identifying and addressing fruad and limiting the impact on legitimate customers. In addition to potential customer alienation, hard costs to be considered include not detecting a fraud, revenue loss from blocking a legitimate sale, and transaction review and chargeback expenses. This is a two part project which first focuses on the planning steps for creating a credit card fraud detection model. Part 2 will include a review of potential predicted models and their associated implementation cost matrix that can then be utilized by merchants to determine the optimal balance between accepting, reviewing or denying transactions. 

The dataset used in the project contains transactions made by credit cards in September 2013 by european cardholders over a two day period of time. It contains 492 fraudulent transactions out of 284,807 total transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It includes 28 potential fraud prediction features which have been anomynized through a PCA dimensionality reduction transformation in order to maintain confidentiality of the data. 

This project has three goals:
1.  Identify features that are most likely to influence a fraud detection model.
2.  Determine if multiple models are needed for detecting different variations of fraud.
3.  Estimate if training a model on Day 1 data will be sufficient for detecting fraud on Day2.


![](img\overview.png) 
