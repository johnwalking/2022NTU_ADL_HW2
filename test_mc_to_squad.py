import json
import os
import sys
import pandas as pd
import numpy as np

with open(sys.argv[1], 'r') as f:
    context = json.load(f)

with open(sys.argv[2], 'r') as f:
    testdata = json.load(f)

result = pd.read_csv(sys.argv[3]) 

All = []
for i in range(len(testdata)):
    tmp = []
    tmp.append(context[testdata[i]["paragraphs"][int(result["relevant"][i])]])
    tmp.append(testdata[i]["question"])
    tmp.append(testdata[i]["id"])
    
    tmp.append(0)
    tmp.append("")
    All.append(tmp)

df = pd.DataFrame(All, columns =["context","question", "id", "answer_start","text"])
df.to_csv(sys.argv[4])
