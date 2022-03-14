# -*- coding: utf-8 -*-
"""Project_P94.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1etX2eULMC8hkgHxDcp-kiGtnabRFYu_M

## Importing Necessary Libraries
"""

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

"""## importing Data"""

incident_data=pd.read_csv('/content/drive/MyDrive/Project_94/incident_event_log.csv')
incident_data

"""## Data Understanding"""

incident_data.shape

list(incident_data.columns)

incident_data=incident_data.replace('?',np.nan)
incident_data

incident_data['incident_state'].unique()

incident_data['incident_state'].replace('-100',np.nan,inplace=True)

incident_data.isna().sum()

na_value=incident_data.isna().sum()

na_value/len(incident_data)

incident_data.info()

"""## Data Cleaning"""

incident_data=incident_data.drop(columns=['sys_created_by','sys_created_at','problem_id','rfc','vendor','caused_by','cmdb_ci'])
incident_data

incident_data=incident_data.dropna(subset=['incident_state','caller_id','opened_by','location','category','subcategory','closed_code','resolved_by','resolved_at'])
incident_data

incident_data.isna().sum()

na_value_1=incident_data.isna().sum()

na_value_1/len(incident_data)

"""
## Filling the NaN values in Column with Mode value of that column"""

incident_data['assignment_group'].value_counts()

incident_data['assignment_group']=incident_data['assignment_group'].fillna('Group 70')
incident_data['assignment_group'].value_counts()

incident_data['u_symptom'].value_counts()

incident_data['u_symptom']=incident_data['u_symptom'].fillna('Symptom 491')
incident_data['u_symptom'].value_counts()

incident_data['assigned_to'].value_counts()

incident_data['assigned_to']=incident_data['assigned_to'].fillna('Resolver 17')
incident_data['assigned_to'].value_counts()

incident_data.isna().sum()

"""## EDA"""

incident_data.groupby(by=['contact_type'])['active'].value_counts().sort_values(ascending = False)

incident_data.groupby(by=['location'])['active'].value_counts().sort_values(ascending = False)

incident_data.groupby(by=['location','active'])['impact'].value_counts().sort_values(ascending = False)

incident_data.groupby(by=['assignment_group','active'])['impact'].value_counts().sort_values(ascending = False)

incident_data.groupby(by=['impact'])['category'].value_counts()

incident_data.groupby(by=['impact'])['resolved_by'].value_counts().sort_values(ascending = False)

incident_data.shape

incident_data.dtypes

incident_data.nunique()

incident_data['incident_state'].value_counts()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

incident_data['active'] = labelencoder.fit_transform(incident_data['active'])
incident_data['made_sla'] = labelencoder.fit_transform(incident_data['made_sla'])
incident_data['knowledge'] = labelencoder.fit_transform(incident_data['knowledge'])
incident_data['u_priority_confirmation'] = labelencoder.fit_transform(incident_data['u_priority_confirmation'])

plt.figure(figsize=(30,15))
plt.subplot(5, 5, 1)
plt.hist(x='incident_state',data=incident_data)
plt.title(label='incident state distribution')

plt.subplot(5, 5, 2)
plt.hist(x='active',data=incident_data)
plt.title(label='active distribution')

plt.subplot(5, 5, 3)
plt.hist(x='reassignment_count',data=incident_data)
plt.title(label='reassignment_count distribution')

plt.subplot(5, 5, 4)
plt.hist(x='reopen_count',data=incident_data)
plt.title(label='reopen_count distribution')

plt.subplot(5, 5, 5)
plt.hist(x='sys_mod_count',data=incident_data)
plt.title(label='sys_mod_count distribution')

plt.subplot(5, 5, 6)
plt.hist(x='made_sla',data=incident_data)
plt.title(label='made_sla distribution')

plt.subplot(5, 5, 7)
plt.hist(x='caller_id',data=incident_data)
plt.title(label='caller_id distribution')

plt.subplot(5, 5, 8)
plt.hist(x='opened_by',data=incident_data)
plt.title(label='opened_by distribution')

plt.subplot(5, 5, 9)
plt.hist(x='sys_updated_by',data=incident_data)
plt.title(label='sys_updated_by distribution')

plt.subplot(5, 5, 10)
plt.hist(x='contact_type',data=incident_data)
plt.title(label='contact_type distribution')

plt.subplot(5, 5, 11)
plt.hist(x='location',data=incident_data)
plt.title(label='location distribution')

plt.subplot(5, 5, 12)
plt.hist(x='category',data=incident_data)
plt.title(label='category distribution')

plt.subplot(5, 5, 13)
plt.hist(x='subcategory',data=incident_data)
plt.title(label='subcategory distribution')

plt.subplot(5, 5, 14)
plt.hist(x='u_symptom',data=incident_data)
plt.title(label='u_symptom distribution')

plt.subplot(5, 5, 15)
plt.hist(x='impact',data=incident_data)
plt.title(label='impact distribution')

plt.subplot(5, 5, 16)
plt.hist(x='urgency',data=incident_data)
plt.title(label='urgency distribution')

plt.subplot(5, 5, 17)
plt.hist(x='priority',data=incident_data)
plt.title(label='priority distribution')

plt.subplot(5, 5, 18)
plt.hist(x='assignment_group',data=incident_data)
plt.title(label='assignment_group distribution')

plt.subplot(5, 5, 19)
plt.hist(x='assigned_to',data=incident_data)
plt.title(label='assigned_to distribution')

plt.subplot(5, 5, 20)
plt.hist(x='knowledge',data=incident_data)
plt.title(label='knowledge distribution')

plt.subplot(5, 5, 21)
plt.hist(x='u_priority_confirmation',data=incident_data)
plt.title(label='u_priority_confirmation distribution')

plt.subplot(5, 5, 22)
plt.hist(x='notify',data=incident_data)
plt.title(label='notify distribution')

plt.subplot(5, 5, 23)
plt.hist(x='closed_code',data=incident_data)
plt.title(label='closed_code distribution')

plt.subplot(5, 5, 24)
plt.hist(x='resolved_by',data=incident_data)
plt.title(label='resolved_by distribution')

plt.show()

incident_data.groupby('closed_code').count()['number'].plot(kind='bar',title='Distribution of closed_code',figsize=(10, 10))
plt.show()
incident_data['closed_code'].value_counts()

incident_data.groupby('incident_state').count()['number'].plot(kind='bar',title='incident state distribution',figsize=(15,10))
plt.show()

"""## Data Visualization"""

sns.countplot(x='active',data=incident_data)
plt.show()

plt.figure(figsize=(7,7))
sns.histplot(incident_data,x='active',hue='impact')
plt.show()

sns.countplot(x='impact',data=incident_data)
plt.show()
incident_data['impact'].value_counts()

sns.countplot(x='urgency',data=incident_data)
plt.show()
incident_data['urgency'].value_counts()

plt.figure(figsize=(15,10))
sns.histplot(incident_data,x='impact',hue='urgency')
plt.show()

sns.countplot(x='priority',data=incident_data)
plt.show()
incident_data['priority'].value_counts()

plt.figure(figsize=(15,10))
sns.histplot(incident_data,x='impact',hue='priority')
plt.show()

sns.countplot(x='contact_type',data=incident_data)
plt.show()
incident_data['contact_type'].value_counts()

plt.figure(figsize=(7,7))
sns.histplot(incident_data,x='contact_type',hue='impact',palette=["C6", "C9", "C0"])
plt.show()

incident_data.category
pd.crosstab(incident_data.category,incident_data.impact).plot(kind="bar",title='category vs impact type',figsize=(20,7))
plt.show()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

incident_data['number'] = labelencoder.fit_transform(incident_data['number'])
incident_data['incident_state'] = labelencoder.fit_transform(incident_data['incident_state'])

incident_data['caller_id'] = labelencoder.fit_transform(incident_data['caller_id'])
incident_data['opened_by'] = labelencoder.fit_transform(incident_data['opened_by'])
incident_data['sys_updated_by'] = labelencoder.fit_transform(incident_data['sys_updated_by'])
incident_data['location'] = labelencoder.fit_transform(incident_data['location'])
incident_data['category'] = labelencoder.fit_transform(incident_data['category'])
incident_data['subcategory'] = labelencoder.fit_transform(incident_data['subcategory'])
incident_data['u_symptom'] = labelencoder.fit_transform(incident_data['u_symptom'])

incident_data['contact_type'] = labelencoder.fit_transform(incident_data['contact_type'])
incident_data['impact'] = labelencoder.fit_transform(incident_data['impact'])
incident_data['urgency'] = labelencoder.fit_transform(incident_data['urgency'])
incident_data['priority'] = labelencoder.fit_transform(incident_data['priority'])
incident_data['assignment_group'] = labelencoder.fit_transform(incident_data['assignment_group'])
incident_data['assigned_to'] = labelencoder.fit_transform(incident_data['assigned_to'])

incident_data['notify'] = labelencoder.fit_transform(incident_data['notify'])
incident_data['closed_code'] = labelencoder.fit_transform(incident_data['closed_code'])
incident_data['resolved_by'] = labelencoder.fit_transform(incident_data['resolved_by'])
incident_data.head(10)

incident_data.dtypes

incident_data=incident_data.drop(columns=['opened_at','sys_updated_at','resolved_at','closed_at'])

incident_data.describe(include='all')

incident_data['incident_state'].unique()

incident_data['reassignment_count'].unique()

incident_data['u_priority_confirmation'].unique()

incident_data['reopen_count'].unique()

incident_data['sys_mod_count'].sort_values().unique()

incident_data['made_sla'].unique()

incident_data['opened_by'].sort_values().unique()

incident_data['contact_type'].unique()

incident_data['location'].sort_values().unique()

incident_data['impact'].unique()

incident_data['urgency'].unique()

incident_data['priority'].unique()

incident_data['category'].sort_values().unique()

incident_data['assignment_group'].sort_values().unique()

incident_data[incident_data.duplicated()]

incident_data.describe(include='all')

incident_data.dtypes

incident_data.info()

correlation=incident_data.corr()
correlation

plt.figure(figsize=(20,15))
sns.heatmap(correlation,annot=True)
plt.show()

plt.figure(figsize=(30,15))
data=incident_data.iloc[:,1:]
data=data.drop(columns=['caller_id'])
sns.boxplot(data=data)
plt.show()

"""## Data Preparation"""

incident_data.reset_index(inplace=True)

y=incident_data['impact']
y

X=incident_data.drop(columns='impact')
X

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=23)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""## Feature Engineering

### Feature selection using Chi-Square used only for the Categorical data
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

ordered_rank_feature=SelectKBest(score_func=chi2,k=24)
ordered_feature=ordered_rank_feature.fit(X_train,y_train)
ordered_feature

df_scores=pd.DataFrame(ordered_feature.scores_,columns=['scores'])
df_columns=pd.DataFrame(X_train.columns)
features_rank=pd.concat([df_scores,df_columns],axis=1)
features_rank.nlargest(10,'scores')

ranked_features=pd.Series(ordered_feature.scores_,index=X_train.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()
ranked_features.nlargest(10)

"""# Feature selection using ExtraTreeClassifier"""

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X_train,y_train)

model.feature_importances_

ranked_features=pd.Series(model.feature_importances_,index=X_train.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()
ranked_features.nlargest(10)

"""# Feature selection using DecisionTreeClassifier"""

from sklearn.tree import DecisionTreeClassifier

DT_class = DecisionTreeClassifier()
DT_class.fit(X_train,y_train)

DT_class.feature_importances_

ranked_features=pd.Series(DT_class.feature_importances_,index=X_train.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()
ranked_features.nlargest(10)

"""# Feature Selection using Mutual information"""

from sklearn.feature_selection import mutual_info_classif
mutual_info = mutual_info_classif(X_train, y_train)
mutual_info

ranked_features=pd.Series(mutual_info,index=X_train.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()
ranked_features.nlargest(10)

"""## Selected the important Features which are obtained from the Feature Selection Process.(Select the Features having more impact on dependent variable.)"""

X=incident_data[['priority','urgency','index','number','opened_by','resolved_by','assigned_to','category','knowledge','location','u_priority_confirmation','reassignment_count']]
X

X.info()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=23)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""## Logistic regression Algorithm

## Model Building
"""

from sklearn.linear_model import LogisticRegression

logistic_model=LogisticRegression()

logistic_model.fit(X_train,y_train)

"""## Model Testing"""

# for train data
y_pred = logistic_model.predict(X_train)

# for test data
y_pred_test = logistic_model.predict(X_test)
y_pred

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train,y_pred)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test,y_pred_test)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train,y_pred))

# for test data
print(accuracy_score(y_test,y_pred_test))

# for train data
print(classification_report(y_train,y_pred))

# for test data
print(classification_report(y_test,y_pred_test))

"""## Balancing The Data"""

from imblearn.over_sampling import SMOTE
sm=SMOTE(random_state=42)
X_train_SMOTE,y_train_SMOTE=sm.fit_resample(X_train,y_train)
X_test_SMOTE,y_test_SMOTE=sm.fit_resample(X_test,y_test)

from collections import Counter
print("Before SMOTE :",Counter(y_train))
print("After SMOTE :",Counter(y_train_SMOTE))

y_train.shape

y_train_SMOTE.shape

"""## Logistic regression Algorithm with Balanced Data

## Model Building
"""

from sklearn.linear_model import LogisticRegression

logistic_model_1=LogisticRegression()

logistic_model_1.fit(X_train_SMOTE,y_train_SMOTE)

"""## Model Testing"""

# for train data
y_pred_1 = logistic_model_1.predict(X_train_SMOTE)

# for test data
y_pred_test_1 = logistic_model_1.predict(X_test_SMOTE)

y_train_SMOTE.shape

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train_SMOTE,y_pred_1)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test_SMOTE,y_pred_test_1)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train_SMOTE,y_pred_1))

# for test data
print(accuracy_score(y_test_SMOTE,y_pred_test_1))

# for train data
print(classification_report(y_train_SMOTE,y_pred_1))

# for test data
print(classification_report(y_test_SMOTE,y_pred_test_1))



"""## Decision Tree Model"""

from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier()

"""## Finding out the best hyperparameter for building the Tree

"""

from sklearn.model_selection import GridSearchCV

#grid_search = GridSearchCV(estimator = dt_model, param_grid = {'criterion':['gini','entropy'],'max_depth':[2,3,4,5,6,7,8,9,10,11,12]} , cv= 5)
#grid_search

#grid_search.fit(X,y)

#grid_search.best_params_

#grid_search.best_score_

dt_model=DecisionTreeClassifier(criterion='entropy',max_depth=6)

dt_model.fit(X_train,y_train)

from sklearn.tree import plot_tree
from matplotlib import pyplot as plt

plt.figure(figsize=(22,12))
plot_tree(dt_model,filled=True, rounded=True)
plt.show()

"""## Model Testing"""

# for train data
y_pred_2=dt_model.predict(X_train)

# for test data
y_pred_test_2=dt_model.predict(X_test)

"""## Confusion_Matrix :- To know the Misclassification done by the model"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train,y_pred_2)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test,y_pred_test_2)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""### The model accuracy """

# for train data
print(accuracy_score(y_train,y_pred_2))

# for test data
print(accuracy_score(y_test,y_pred_test_2))

# for train data
print(classification_report(y_train,y_pred_2))

# for test data
print(classification_report(y_test,y_pred_test_2))



"""## Decision Tree Model With balanced Data"""

from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier()

"""## Finding out the best hyperparameter for building the Tree

"""

from sklearn.model_selection import GridSearchCV

#grid_search = GridSearchCV(estimator = dt_model, param_grid = {'criterion':['gini','entropy'],'max_depth':[2,3,4,5,6,7,8,9,10,11,12]} , cv= 5)
#grid_search

#grid_search.fit(X,y)

#grid_search.best_params_

#grid_search.best_score_

dt_model=DecisionTreeClassifier(criterion='entropy',max_depth=6)

dt_model.fit(X_train_SMOTE,y_train_SMOTE)

from sklearn.tree import plot_tree
from matplotlib import pyplot as plt

plt.figure(figsize=(22,12))
plot_tree(dt_model,filled=True, rounded=True)
plt.show()

"""## Model Testing"""

# for train data
y_pred_3=dt_model.predict(X_train_SMOTE)
y_pred_3=pd.DataFrame(y_pred_3)
y_pred_3
# for test data
y_pred_test_3=dt_model.predict(X_test_SMOTE)
y_pred_test_3=pd.DataFrame(y_pred_test_3)
y_pred_test_3

X_test_SMOTE['Prediction']=y_pred_test_3
X_test_SMOTE

"""## Confusion_Matrix :- To know the Misclassification done by the model"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train_SMOTE,y_pred_3)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test_SMOTE,y_pred_test_3)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""### The model accuracy """

# for train data
print(accuracy_score(y_train_SMOTE,y_pred_3))

# for test data
print(accuracy_score(y_test_SMOTE,y_pred_test_3))

# for train data
print(classification_report(y_train_SMOTE,y_pred_3))

# for test data
print(classification_report(y_test_SMOTE,y_pred_test_3))



"""## Random Forest Algorithm"""

from sklearn.ensemble import RandomForestClassifier

rf_model=RandomForestClassifier()

#grid_search=GridSearchCV(rf_model,param_grid={'criterion':['gini','entropy'],'max_depth':[2,3,4,5,6,7,8,9,10,11,12]},cv=5)
#grid_search

#grid_search.fit(X,y)

#grid_search.best_params_

#grid_search.best_score_

"""## Model Training"""

rf_model=RandomForestClassifier(criterion='entropy',max_depth=3)

rf_model.fit(X_train,y_train)

"""## Model Testing"""

y_pred_4= rf_model.predict(X_train)

y_pred_test_4= rf_model.predict(X_test)

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train,y_pred_4)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test,y_pred_test_4)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train,y_pred_4))

# for test data
print(accuracy_score(y_test,y_pred_test_4))

# for train data
print(classification_report(y_train,y_pred_4))

# for test data
print(classification_report(y_test,y_pred_test_4))



"""## Balancing The Data"""

from imblearn.over_sampling import SMOTE
sm=SMOTE(random_state=42)
X_train_SMOTE,y_train_SMOTE=sm.fit_resample(X_train,y_train)
X_test_SMOTE,y_test_SMOTE=sm.fit_resample(X_test,y_test)

from collections import Counter
print("Before SMOTE :",Counter(y_train))
print("After SMOTE :",Counter(y_train_SMOTE))

y_train.shape

y_train_SMOTE.shape

"""## Random Forest Algorithm with balanced data"""

from sklearn.ensemble import RandomForestClassifier

rf_model=RandomForestClassifier()

#grid_search=GridSearchCV(rf_model,param_grid={'criterion':['gini','entropy'],'max_depth':[2,3,4,5,6,7,8,9,10,11,12]},cv=5)
#grid_search

#grid_search.fit(X,y)

#grid_search.best_params_

#grid_search.best_score_

"""## Model Training"""

rf_model=RandomForestClassifier(criterion='gini',max_depth=3)

rf_model.fit(X_train_SMOTE,y_train_SMOTE)

"""## Model Testing"""

y_pred_5= rf_model.predict(X_train_SMOTE)

y_pred_test_5= rf_model.predict(X_test_SMOTE)

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train_SMOTE,y_pred_5)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test_SMOTE,y_pred_test_5)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train_SMOTE,y_pred_5))

# for test data
print(accuracy_score(y_test_SMOTE,y_pred_test_5))

# for train data
print(classification_report(y_train_SMOTE,y_pred_5))

# for test data
print(classification_report(y_test_SMOTE,y_pred_test_5))

"""## Knn Algorithm"""

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

st_scaler=StandardScaler()

scale_data=st_scaler.fit_transform(X)
X=pd.DataFrame(scale_data,columns=['priority','urgency','index','number','opened_by','resolved_by','assigned_to','category','knowledge','location','u_priority_confirmation','reassignment_count'])
X.head(4)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=23)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

Knn_model=KNeighborsClassifier()

from sklearn.model_selection import cross_val_score
CV_Scores = []
for i in range(1,18,1):
  knn_model = KNeighborsClassifier(n_neighbors=i)
  cross_validation_score = cross_val_score(estimator = knn_model,X=X,y=y,cv=6)
  CV_Scores.append(cross_validation_score.mean())

CV_Scores

sns.lineplot(range(1,18,1),CV_Scores)
plt.title('Neighbours Vs CVScore')
plt.xlabel('Neighbours')
plt.ylabel('Mean Accuracy')
plt.show()

CV_Scores.index(max(CV_Scores))

"""**Index 1 corresponds to the 13 Neighbours so it is the Optimal Number for this data.**

## Model Preparation
"""

knn_model = KNeighborsClassifier(n_neighbors=13)

"""## Model Training"""

knn_model.fit(X_train,y_train)

y_pred_6 =knn_model.predict(X_train)

y_pred_test_6 =knn_model.predict(X_test)

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train,y_pred_6)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test,y_pred_test_6)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train,y_pred_6))

# for test data
print(accuracy_score(y_test,y_pred_test_6))

# for train data
print(classification_report(y_train,y_pred_6))

# for test data
print(classification_report(y_test,y_pred_test_6))



"""## Support Vector Machines Algorithm"""

from sklearn.svm import SVC

svm_model=SVC(kernel='linear')

svm_model.fit(X_train,y_train)

"""## model Prediction"""

y_pred_7=svm_model.predict(X_train)

y_pred_test_7=svm_model.predict(X_test)

"""## Model Evaluation

## Confusion_Matrix :- To know the Misclassification done by the model
"""

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
# for train data
mat_train=confusion_matrix(y_train,y_pred_7)
mat_train

ax= sns.heatmap(mat_train, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

# for test data
mat_test=confusion_matrix(y_test,y_pred_test_7)
mat_test

ax= sns.heatmap(mat_test, annot=True,fmt='g')
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Impact')
ax.set_ylabel('Actual Impact')
plt.show()

"""## The model accuracy """

# for train data
print(accuracy_score(y_train,y_pred_7))

# for test data
print(accuracy_score(y_test,y_pred_test_7))

# for train data
print(classification_report(y_train,y_pred_7))

# for test data
print(classification_report(y_test,y_pred_test_7))

"""## Model Deployment"""

from pickle import dump

dump(dt_model, open('dt_model_app.pkl','wb'))

