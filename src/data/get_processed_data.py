import numpy as np
import pandas as pd
import os

def read_data():
    # Set path for raw data and read file
    raw_file_path = os.path.join(os.path.pardir, 'data', 'raw')
    train_file_path = os.path.join(raw_file_path, 'train.csv')
    test_file_path = os.path.join(raw_file_path, 'test.csv')
    # Read the data with all default parameters
    train_df = pd.read_csv(train_file_path, index_col='PassengerId')
    test_df = pd.read_csv(test_file_path, index_col='PassengerId')
    test_df['Survived'] = -999
    df = pd.concat((train_df, test_df), axis = 0)
    return df

def process_data(df):
    # Using method chaining concept:
    return (df
            # Create title attribute - then add this
            .assign(Title = lambda x: x.Name.map(getTitleFromName))
            # working for missing values
            .pipe(fill_missing_values)
            # Create fare bin feature
            .assign(Fare_Bin = lambda x: pd.qcut(x.Fare, 4, labels = ['very_low','low','high','very_high']))
            # Create age state:
            .assign(AgeState =  lambda x: np.where(x.Age >= 18, 'Adult', 'Child'))
            .assign(FamilySize = lambda x: x.Parch + x.SibSp + 1)  # +1 for self)
            .assign(IsMother = lambda x: np.where((x.Sex == 'female') & (x.Age > 18) & (x.Title != 'Miss') & (x.Parch > 0), 1, 0))
            # Create deck feature
            .assign(Cabin = lambda x: np.where(x.Cabin == 'T' ,np.nan, x.Cabin))
            .assign(Deck = lambda x: x.Cabin.map(get_deck))
            # Feature encoding:
            .assign(IsMale =  lambda x: np.where(x.Sex == 'male', 1, 0))
            .pipe(pd.get_dummies, columns = ['Deck','Pclass','Title','Fare_Bin','Embarked','AgeState'])
            # add code to drop unecessary columns
            .drop(['Cabin', 'Name', 'Ticket', 'Parch', 'SibSp', 'Sex'], axis =1)
            # reorder columns
            .pipe(reorder_columns)
                    
    )
def getTitleFromName(name):
    titleGroup = {
        'mr': 'Mr',
        'mrs' : 'Mrs', 
        'miss': 'Miss', 
        'master': 'Master', 
        'don': 'Sir', 
        'rev': 'Sir', 
        'dr': 'Officer', 
        'mme': 'Mrs' ,
        'ms': 'Mrs',
        'major': 'Officer',  
        'lady': 'Lady', 
        'sir': 'Sir', 
        'mlle': 'Mrs', 
        'col': 'Officer',  
        'capt': 'Officer',  
        'the countess': 'Lady',
        'jonkheer': 'Sir', 
        'dona': 'Lady'
    }
    first_name_with_title = name.split(',')[1]
    title = first_name_with_title.split('.')[0]
    title = title.strip().lower()
    return titleGroup[title]

def fill_missing_values(df):
    #embarked 
    df.Embarked.fillna('C', inplace = True)
    # fare
    median_fare =df[(df.Pclass == 3) & (df.Embarked == 'S')].Fare.median()
    df.Fare.fillna(median_fare, inplace = True)
    # age
    title_age_median = df.groupby('Title').Age.transform('median')
    df.Age.fillna(title_age_median, inplace = True)
    return df

def reorder_columns(df):
    columns = [column for column in df.columns if column != 'Survived']
    columns = ['Survived'] + columns
    df = df[columns]
    return df

def get_deck(cabin):
    return np.where(pd.notnull(cabin), str(cabin)[0].upper(), 'Z')

def write_data(df):
    processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
    write_train_path = os.path.join(processed_data_path, 'train.csv')
    write_test_path = os.path.join(processed_data_path, 'test.csv')
    # train data:
    df.loc[df.Survived != -999].to_csv(write_train_path)
    # test data:
    columns = [column for column in df.columns if column != 'Survived']
    df.loc[df.Survived == -999, columns].to_csv(write_test_path)

if __name__ == '__main__':
    df = read_data()
    df = process_data(df)
    write_data(df)