# import dataset for reading  
from pandas import read_csv

# "./Dataset/data_banknote_authentication.csv"
def load_data(file_name):
    # file_name = (not file_name) 
    # read file into dataframe
    dataset = read_csv(file_name)
    dataset = dataset.sample(frac=1).reset_index(drop=True)
    print(dataset)
    X = dataset.drop("label", axis=1)
    y = dataset["label"]
    return X, y
