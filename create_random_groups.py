#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
from datetime import datetime

emails = pd.read_excel("../Students emails.xlsx")

persons_per_group = 5
groups = []
students_left = set(emails['NAME'].tolist())
n_groups = (len(students_left) // persons_per_group) + 1

group_df_data = []

for i in range(n_groups):
    if len(students_left) > 5:
        g = set(np.random.choice(list(students_left), replace=False, size=persons_per_group).tolist())
    else:
        g = set(students_left)
    students_left -= g
    groups += [g]
    
    for student_email in g:
        group_df_data += [{'Group': i+1, 'Student': student_email}]
    
if len(groups[-1]) < 5:
    _extra = groups.pop()
    for _name in _extra:
        _random_group = np.random.choice(range(n_groups-1))
        groups[_random_group].add(_name)
        group_df_data += [{'Group': _random_group+1, 'Student': _name}]
    
group_df = pd.DataFrame(group_df_data, columns=['Group', 'Student'])
    
# for i, g in enumerate(groups):
#     print(f"Group {i+1}")
#     for e in g:
#         print(e)
#     print()

group_df = group_df.sort_values('Group')
_today_date = datetime.date(datetime.now())
group_df
group_df.to_csv(f"./Groups_{_today_date}.csv")


# In[ ]:




