import json
import os
import sys
with open( sys.argv[1],'r') as f:
    context = json.load(f)

with open(sys.argv[2], 'r') as f:
    testdata = json.load(f)

import pandas as pd
import numpy as np

All = []

for i in range(len(testdata)):
    tmp = []
    tmp.append( testdata[i]["id"] )
    tmp.append( testdata[i]["id"] )
    tmp.append(  testdata[i]["question"])
    tmp.append(  testdata[i]["question"])
    tmp.append(  testdata[i]["question"])
    tmp.append(  "gold" )
    #answer = 0
    for j  in range(len(testdata[i]["paragraphs"])):
      #if int(traindata[i]["paragraphs"][j]) == int(traindata[i]['relevant']):
        #answer = j
      tmp.append(  context[int(testdata[i]["paragraphs"][j])] )
    tmp.append(0)

    All.append(tmp)
df = pd.DataFrame(All, columns = ["video-id" ,"fold-ind" ,"startphrase", "sent1","sent2", "gold-source", "ending0","ending1","ending2","ending3","labels"] )

#small = df[:2]
#small.to_csv('./test_small.csv')
df.to_csv(sys.argv[3])


