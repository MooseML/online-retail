# Holiday Shopper Segmentation: Clustering, Frequent Itemset Mining, & Recommendations

## Table of Contents
- [Overview](#overview)
- [Project Goals](#project-goals)
- [Dataset](#dataset)
- [Methods](#methods)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

---

## Overview
This projects topic is to group holiday shoppers into meaningful segments using unsupervised learning techniques. Businesses that understand customer behavior, especially during peak shopping seasons, can adjust their marketing strategies more effectively. After exploring this e-commerce dataset and noticing that the majority of purchases occur in November and December, I decided to focus on holiday time period transactions. Because there are no explicit labels for holiday shopper type, clustering is a great approach to discover these segments.


## Project Goals
The primary goal is to apply **K-Means** and **Hierarchical Clustering** to segment holiday shoppers into distinct groups:

 - Non-Holiday Shoppers (low holiday purchases and spending)
 - Moderate Holiday Shoppers (moderate holiday purchases and spending)
 - Frequent Holiday Shoppers (high holiday purchases and spending)

By identifying these clusters, this business can personalize promotions, recommend relevant products, and develop targeted marketing campaigns to boost sales. In addition to clustering, **Frequent Itemset Mining** (via FPGrowth) will discover which items often occur together, supporting a simple **rule-based recommendation system** that suggests products frequently purchased together.

Finally, I will also show a more advanced **recommender using implicit feedback** (purchased vs. not purchased) with the implicit library. This dual approach of simple rule-based and implicit collaborative filtering recommenders highlights two different methods for making product suggestions to holiday shoppers.

## Dataset
- **Source:** The data used in this project is sourced from the [UC Irvine Machine Learning Repository: Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail). It is a publicly available dataset provided by a UK-based and registered online retail company. The data can be downloaded from the link above.

- **Details:** 
The dataset contains 8 features and 541,909 rows of customer data, with a total size of  **23.7 MB**. Each row represents a transaction, and the columns represent attributes about the transaction. Transactions ocurred from December 1, 2010 to December 31, 2011.

- **Number of rows (samples):** 541,909  
- **Number of columns (features):** 8  
- **Data Size:** ~23.7 MB

**Key Features:**
- **Categorical Features:** `InvoiceNo`, `StockCode`, `Description`,  `InvoiceDate`, `CustomerID`, `Country`
- **Numerical Features:** `Quantity`, `UnitPrice`

**Context:**  
The retailer specializes in unique gifts and sold through catalogs and phone orders before transitioning online two years before this datasets creation. This dataset has a large number of transactions, primarily in the UK and Europe over a 13-month period, making it a good source for understanding customer behavior.

## Methods
1. Problem Definition and Data Gathering
2. Exploratory Data Analysis (EDA)
3. Model Building and Analysis
4. Discussion and Conclusion
   
## Results
- **Best Model:** [K-Means] Produced balanced clusters, enabling meaningful frequent itemset mining.
- **Performance:**
  - Silhouette Score for k=3: 0.621
  - Calinski-Harabasz Index: 1893.315
  - Davies-Bouldin Score: 0.884
- **Frequent Itemset Mining:**
Non-Holiday Shoppers: 25 itemsets; e.g., "PAPER CHAIN KIT VINTAGE CHRISTMAS" → "PAPER CHAIN KIT 50'S CHRISTMAS" (confidence = 0.61, lift = 5.12).
Frequent Holiday Shoppers: 33 itemsets; e.g., "HAND WARMER RED RETROSPOT" → "HAND WARMER UNION JACK" (confidence = 0.89, lift = 13.18).
Moderate Holiday Shoppers: 45 itemsets; e.g., "ALARM CLOCK BAKELIKE GREEN" → "ALARM CLOCK BAKELIKE RED" (confidence = 0.72, lift = 10.97).
- **Recommender Results:**
Rule-Based: Transparent recommendations like "HAND WARMER UNION JACK" for "HAND WARMER RED RETROSPOT."
ALS Implicit: Best hyperparameters (factors = 19, regularization = 0.077, iterations = 13). Recommendations tailored by cluster, e.g., "ALARM CLOCK BAKELIKE IVORY" with high relevance scores for Cluster 0 shoppers.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MooseML/online-retail.git

2. Navigate to the project directory:
   ```bash
   cd online_retail

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook clustering_holiday_shoppers.ipynb
   
2. Follow the steps in the notebook to reproduce the analysis.

## Acknowledgments

- **Dataset:** This project utilizes the[UC Irvine Machine Learning Repository: Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)  
