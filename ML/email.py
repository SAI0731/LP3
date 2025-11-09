import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,accuracy_score , confusion_matrix

df = pd.read_csv('emails.csv')
print(df.columns)
print(df.head())
print(df['Prediction'].value_counts())
X = df.drop(columns= ['Prediction','Email No.'])
y = df['Prediction']


X_train , X_test , y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train,y_train)
knn_pred = knn.predict(X_test)

print("-------svc----------")
print("accuracy: ", accuracy_score(y_test,knn_pred))
print("confusion matrix: \n", confusion_matrix(y_test,knn_pred))
print("classification report: \n", classification_report(y_test,knn_pred))

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

print("-------svc----------")
print("accuracy: ", accuracy_score(y_test,svm_pred))
print("confusion matrix: \n", confusion_matrix(y_test,svm_pred))
print("classification report: \n", classification_report(y_test,svm_pred))