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
        dict = sliced_data.to_dict()
        return json.dumps(dict)
