import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/movies.csv', header=None)

df.columns = ['S. No', 'Movie Name', 'Release Year', 'IMDb Rating', 'Duration']

print(df)