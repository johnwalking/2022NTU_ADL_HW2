import json
import os
import sys

with open(sys.argv[1], 'r') as f:
    context = json.load(f)

with open(sys.argv[2], 'r') as f:
    data = json.load(f)

import pandas as pd
import numpy as np 

All = []
for i in range(len(data)):
    tmp = []
    tmp.append(context[int(data[i]["relevant"])])
    tmp.append(data[i]["question"])
    tmp.append(data[i]["id"])
    """
    T = {}
    T["text"] = [data[i]["answer"]["text"]]
    T["answer_start"] = [data[i]["answer"]["start"]]
    """
    tmp.append(data[i]["answer"]["start"])
    tmp.append(data[i]["answer"]["text"])
    #tmp.append(T)
    All.append(tmp)

df = pd.DataFrame(All, columns =["context","question", "id", "answer_start","text"])
df.to_csv(sys.argv[3])

