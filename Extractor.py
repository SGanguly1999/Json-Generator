import random
import json
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

class Extractor:
    def __init__(self,dataset,maximum_observs):
        self.data = pd.read_csv(dataset)
        self.currRow = 0
        self.maxObs = maximum_observs
    def extract(self):
        numOfObs = random.randint(1,self.maxObs)
        sliced_data = self.data.iloc[self.currRow:self.currRow+numOfObs]
        self.currRow += numOfObs
        json_res = []
        for index, row in sliced_data.iterrows():
            json_res.append(row.to_dict())
        return json.dumps(json_res)
    def extract1(self):
        numOfObs = random.randint(1, self.maxObs)
        sliced_data = self.data.iloc[self.currRow:self.currRow + numOfObs]
        self.currRow += numOfObs
        json_res = []
        dict ={}
        for col in sliced_data:
            dict[col]=list(sliced_data[col])
        return json.dumps(dict)
    def extract2(self):
        numOfObs = random.randint(1, self.maxObs)
        sliced_data = self.data.iloc[self.currRow:self.currRow + numOfObs]
        self.currRow += numOfObs
        return json.dumps(sliced_data.to_dict())
