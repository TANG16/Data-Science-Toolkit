import pandas as pd 


pd.read_csv()
pd.crosstab()
pd.value_counts().to_dict
<<<<<<< HEAD

import pandas_profiling as pdp
pdp.ProfileReport(df)


#See individual values 

lst = []
for column in columns:
  column = df_categorical[column].value_counts()
  lst.append(column)
  print("{column} \n")
=======
>>>>>>> cd3dda03879bf3a61ce1675ebb4b5d098d8755d7
