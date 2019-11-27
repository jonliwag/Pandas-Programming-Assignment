import pandas as pd
cars = pd.read_csv("cars.csv")

a = cars.iloc[ : , 1: :2].head(5)
b = cars[:1]
c = cars.loc[[23],['Model','cyl']]
d = cars.loc[[1,18,28],['Model','cyl','gear']]