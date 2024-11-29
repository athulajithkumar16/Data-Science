# pandas Data Structure
'''
1. Series       : 1 Dimension Data eg : list, tuple, dict
2. Data Frame   : 2 Dimension Data eg : nested_list, nested_dict, text, csv
3. Label        : 3 Dimensional Data
'''

import pandas as pd

s = pd.Series([3,4,5,6])

print(s)
print(s.dtype)
print(s.size)
print(s.shape)
