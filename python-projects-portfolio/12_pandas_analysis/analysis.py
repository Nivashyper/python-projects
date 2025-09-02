import pandas as pd

df = pd.DataFrame({
    "month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "sales": [10,12,8,15,18,20],
})
print(df.describe())
print("Max month:", df.loc[df['sales'].idxmax(), 'month'])
