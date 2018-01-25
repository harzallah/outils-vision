import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import re

# Define function to extract titles from passenger names
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # If the title exists, extract and return it.
    if title_search:
        return title_search.group(1)
    return ""

def transform_data(dataset):
    # Feature that tells whether a passenger had a cabin on the Titanic
    dataset['Has_Cabin'] = dataset["Cabin"].apply(lambda x: 0 if type(x) == float else 1)

    # Feature engineering steps taken from Sina
    # Create new feature FamilySize as a combination of SibSp and Parch
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    # Create new feature IsAlone from FamilySize
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1
    # Remove all NULLS in the Embarked column
    dataset['Embarked'] = dataset['Embarked'].fillna('S')
    # Remove all NULLS in the Fare column and create a new feature CategoricalFare
    dataset['Fare'] = dataset['Fare'].fillna(train['Fare'].median())
    #### train['CategoricalFare'] = pd.qcut(train['Fare'], 4)
    # Create a New feature CategoricalAge
    age_avg = dataset['Age'].mean()
    age_std = dataset['Age'].std()
    age_null_count = dataset['Age'].isnull().sum()
    age_null_random_list = np.random.randint(age_avg - age_std, age_avg + age_std, size=age_null_count)
    dataset['Age'][np.isnan(dataset['Age'])] = age_null_random_list
    dataset['Age'] = dataset['Age'].astype(int)
    ###### train['CategoricalAge'] = pd.cut(train['Age'], 5)



    # Create a new feature Title, containing the titles of passenger names
    dataset['Title'] = dataset['Name'].apply(get_title)
    # Group all non-common titles into one single grouping "Rare"
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    
    # Mapping Sex
    dataset['Sex'] = dataset['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
    
    # Mapping titles
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)
    
    # Mapping Embarked
    dataset['Embarked'] = dataset['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)
    
    # Mapping Fare
    dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] 						        = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare']   = 2
    dataset.loc[ dataset['Fare'] > 31, 'Fare'] 							        = 3
    dataset['Fare'] = dataset['Fare'].astype(int)
    
    # Mapping Age
    dataset.loc[ dataset['Age'] <= 10, 'Age0'] 					       = 1
    dataset.loc[(dataset['Age'] > 10) & (dataset['Age'] <= 18), 'Age1'] = 1
    dataset.loc[(dataset['Age'] > 18) & (dataset['Age'] <= 25), 'Age2'] = 1
    dataset.loc[(dataset['Age'] > 25) & (dataset['Age'] <= 32), 'Age3'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age4'] = 1
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age5'] = 1
    dataset.loc[ dataset['Age'] > 64, 'Age6'] = 1 ;
    
    dataset.loc[ dataset['Age0'] != 1, 'Age0'] = 0 ;
    dataset.loc[ dataset['Age1'] != 1, 'Age1'] = 0 ;
    dataset.loc[ dataset['Age2'] != 1, 'Age2'] = 0 ;
    dataset.loc[ dataset['Age3'] != 1, 'Age3'] = 0 ;
    dataset.loc[ dataset['Age4'] != 1, 'Age4'] = 0 ;
    dataset.loc[ dataset['Age5'] != 1, 'Age5'] = 0 ;
    dataset.loc[ dataset['Age6'] != 1, 'Age6'] = 0 ;

train = pd.read_csv('train.csv')

#~ ypassengerid = test['PassengerId']

transform_data(train)

drop_elements = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'SibSp', 'Age']

train = train.drop(drop_elements, axis = 1)

print train.head(3)
x_train = train.values

print x_train
