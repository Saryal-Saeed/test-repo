                   
from sklearn import datasets
import pandas as pd

# load_boston() returns sklearn.utils.Bunch
boston_data = datasets.load_boston()
# boston_data.data is a 2D array
# boston_data.feature_names is an array of columns labels
df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
df_boston['target'] = pd.Series(boston_data.target)
df_boston.head()

                

            