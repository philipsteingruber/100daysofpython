import pandas as pd

data = pd.read_csv('squirrel_census.csv')

data['Primary Fur Color'].value_counts().to_csv('fur_colors.csv')