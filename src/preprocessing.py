import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

"""
preprocess_data(filename, datasetid)

Take a dataset's filename along side with the id
and process it so that it will return the
- Features and label
- train data, test data, and validation data
"""


def preprocess_data(filename, datasetid):
    # Load the dataset
    data = pd.read_csv(filename)

    # Fill empty values with 'False'
    data = data.fillna(value=False)

    # X (feature) = Drop the defects column
    # y (label) = Set the 'defects' as the Target label
    X = pd.DataFrame(data.drop(["defects"], axis=1))
    y = pd.DataFrame(data["defects"])
    y *= 1

    # Handle the imbalanced dataset
    sm = SMOTE(random_state=1234, k_neighbors=5)  # for oversampling minority data
    X, y = sm.fit_resample(X, y)
    X = pd.DataFrame(X, columns=X.columns)
    y = pd.DataFrame(y, columns=y.columns)

    # Split the data train and data test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1234
    )
    X_train, X_validation, y_train, y_validation = train_test_split(
        X_train, y_train, test_size=0.20, random_state=1234
    )

    total_data = X_train.copy()
    total_data["defects"] = y_train

    # Plot the heatmap
    corr = total_data.corr()
    sns.set(font_scale=0.5)
    plt.margins()
    sns.heatmap(corr, xticklabels=1, yticklabels=1)
    plt.savefig("figures/correlation" + "_" + str(datasetid) + "_" + str(filename[9:12]) + ".jpg")
    # plt.show()

    return X, y, X_train, X_test, X_validation, y_train, y_test, y_validation


# Change the dataset here, datasetid start from 0
preprocess_data("datasets/cm1.csv", 5)
