**CREDIT SCORE CLASSIFICATION**

https://github.com/MythiliPa/Credit-score-classification-project/assets/142904439/b4335187-6c0b-4829-b598-cd31c57512e9




https://github.com/MythiliPa/Credit-score-classification-project/assets/142904439/5522ddf4-aa20-4b67-8e29-3afd8613c779


Financial sectors and banking have to keenly watch the customer’s credit score. It gives them a big picture of an idea to decide whether they are eligible to sanction a loan or not. Traditional credit scoring models like FICO served well to analyze the credit risk with minimum data. There is a history of so many factors which are uncovered by the traditional models. Hence alternative credit scoring models enter into the business. Machine learning algorithms help to analyze large amounts of data and predict creditworthiness by enhancing the quality of credit scores, i.e., Standard, Good and Poor.

**OBJECTIVE**

This project aims to build a machine-learning model to predict credit scores.

**METHODOLOGY**

The Kaggle dataset has been taken to build the model to classify the credit scores as Standard, good, or poor. The dataset contains 27 features and credit score is the target variable. The train data has been subjected to data preprocessing, feature engineering and model training. The train data is split as 70-30 for validation of test data. Separate test data was subjected to test the model.

**Data reading:**

The dataset was downloaded from Kaggle. As a first step, read the csv file into the DataFrame.

**EDA:**

The data was studied for any duplicates and null values. Boxplot was plotted to study relationships between variables.

**Data preprocessing:**

The categorical target variable was transformed into a numerical type. “Good” is 0, “Standard” is 1 and “Poor” is 2.

The dataset was split into two -train data and test data in the ratio of 70% & 30% by using the

The numerical and categorical columns were separated.

\-Feature encoding:

There are three common ways of encoding, i.e., label encoding, ordinal encoding and one hot encoding.

Label encoding applies to target variables.

Ordinal encoding is used when the variables are in order. One hot encoding is used for unordered variables and it is mapped with binary variables as 0 and 1.

Here, in this project, an ordinal encoder was used, since the order of the categorical variables has to be considered.

\-Feature scaling:

Robust scaler algorithm was used because this scaling method is robust to outliers.

**Model training:**

To create the model, a decision tree classifier and random forest classifier algorithm were used.

Evaluation metrics:

Then the model was evaluated with metrics as accuracy_score().

**Result:**

Since, the data has multiple features, a random forest classifier will be best fit and evaluated with 82% accuracy.

By using the test data, the target variables were predicted, and the output as

|           | **0** |
|-----------|-------|
| **0**     | 0     |
| **1**     | 0     |
| **2**     | 0     |
| **3**     | 0     |
| **4**     | 0     |
| **...**   | ...   |
| **49995** | 1     |
| **49996** | 1     |
| **49997** | 1     |
| **49998** | 2     |
| **49999** | 1     |

50000 rows × 1 columns
