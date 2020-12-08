import pandas as pd 


pd.read_csv()
pd.crosstab()
pd.value_counts().to_dict

import pandas_profiling as pdp
pdp.ProfileReport(df)


#See individual values 

lst = []
for column in columns:
  column = df_categorical[column].value_counts()
  lst.append(column)
  print("{column} \n")