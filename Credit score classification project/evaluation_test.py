import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

def evaluvation_metrics(x_test_path,y_test_path,model):

    #Read data
    X=pd.read_csv(x_test_path)
    y_target=pd.read_csv(y_test_path)
    #seperate numerical and categorical columns
    numerical_columns=X.select_dtypes(exclude='object')
    categorical_columns=X.select_dtypes(include='object')
    
    # categorical -- encoding
    encoder_model=load('ordinal_encoder.pkl')
    col=encoder_model.get_feature_names_out()
    transform=encoder_model.transform(categorical_columns)
    categorical_data_ord=pd.DataFrame(transform,columns=col)
                       
    # numerical-- Scalling
    model_scaling=load('robust_scaler.pkl')
    scaled_data=model_scaling.transform(numerical_columns)
    numerical_scaled_data=pd.DataFrame(scaled_data,columns=numerical_columns.columns)

    # concat numerical and categorical data
    #Features1=pd.concat([categorical_data_ord,categorical_data_ohe],axis=1)
    Features=pd.concat([categorical_data_ord,numerical_scaled_data],axis=1)


    # model testing
    log_reg=load(model)
    y_pred=pd.DataFrame(log_reg.predict(Features))
    test_score=accuracy_score(y_target, y_pred)*100
    
    
    return y_pred, test_score