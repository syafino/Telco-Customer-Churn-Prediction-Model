# Telco-Customer-Churn-Prediction-Model
Predicting customer churn using machine learning on the Telco dataset. This project showcases end-to-end data science skills: from cleaning raw data to training models and interpreting results.
Dataset from: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Python, Pandas, NumPy
scikit-learn (Logistic Regression, Random Forest)
Matplotlib, Seaborn (for visualization)

Data Preprocessing
1.Removed customer ID column
2.Converted TotalCharges to numeric (with error coercion)
3.Handled missing values (NaN) by dropping incomplete rows
4.One-hot encoded categorical features
5.Addressed class imbalance using class_weight='balanced'

Achieved 80%+ accuracy and analyzed precision/recall trade-offs for imbalanced classification.
Visualized key drivers of churn using feature importance plots, enabling business interpretability.

