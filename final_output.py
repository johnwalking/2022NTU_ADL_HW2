import json
import pandas as pd
import sys
with open(sys.argv[1],encoding='utf-8') as f:
    data = json.load(f)

All =[]
for key, value in data.items():
    tmp = []
    tmp.append(key)
    tmp.append(value)
    All.append(tmp)

df = pd.DataFrame(All, columns=["id", "answer"])
df.to_csv(sys.argv[2], index = False)

