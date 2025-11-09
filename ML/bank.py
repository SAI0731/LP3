import pandas as pd
import numpy as np 
df=pd.read_csv(r"C:\Users\sarth\Desktop\Datasets\Churn_Modelling.csv")
df

#Remove the attributes unique to the customer
df=df.drop(['CustomerId','Surname','RowNumber'],axis=1)
#Data preprocessing
df.isnull().sum()


#Converting categorical variable into binary variable 
gender=pd.get_dummies(df['Gender'],drop_first=True)
geography=pd.get_dummies(df['Geography'],drop_first=True)
df=pd.concat([df,gender,geography],axis=1)
df.drop(['Gender','Geography'],axis=1)

#Normalization and Scaling 
#Select Dependent and independent Variable 
X=df.drop(['Exited'],axis=1)
Y=df['Exited']

df

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
X

df.columns

#train_test_split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y)
from sklearn.neural_network import MLPClassifier
model=MLPClassifier()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
#Model Evaluation
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
print("Confusion Matrix: ",confusion_matrix(y_test,y_pred))
print("acccuracy score: ",accuracy_score(y_test,y_pred))
print("Classification Report",classification_report(y_test,y_pred))