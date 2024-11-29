import pandas as pd

# Left Outer Joining
#   returns all the row from left dataFrame, plus matched values
#   from right dataFrame or NULL in case of no matching value.
# df3 = pd.merge(df1, df2, on='id', how='left')

# Right Outer Joining
#   returns all the row from right DataFrame, plus matched values
#   from right dataFrame or NULL in case of no matching value.
# df3 = pd.merge(df1, df2, on='id', how='right')

# Full Outer Joining
#   combination of Left Outer Joining & Right Outer Joining
# df3 = pd.merge(df1, df2, on='id', how='outer')