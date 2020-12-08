
#Replace string for None
#Use df.replace({value: None}) instead of df.replace(value, None)
#This is equivalent to s.replace(to_replace={'a': None}, value=None, method=None)
for i in range(1, 3):
    df.replace({"Missing_" + str(i): None}, inplace=True)