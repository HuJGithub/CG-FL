import math
import numpy as np
import pandas as pd
from data_process.ProcessedData import ProcessedData

class Slice(ProcessedData):

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.rest_columns = raw_data.rest_columns

    def process(self):
        if len(self.label_df) > 1:
            equal_zero_index = (self.label_df != 1).values
            equal_one_index = ~equal_zero_index

            #pass_feature = np.array(self.feature_df[equal_zero_index])
            fail_feature = np.array(self.feature_df[equal_one_index])

            ex_index=[]
            for temp in fail_feature:
                for i in range(len(temp)):
                    if temp[i]==0:
                        ex_index.append(i)
            select_index=[]
            for i in range(len(self.feature_df.values[0])):
                if i not in ex_index:
                    select_index.append(i)

            select_index=list(set(select_index))

            sel_feature = self.feature_df.values.T[select_index].T

            columns = self.feature_df.columns[select_index]

            self.feature_df = pd.DataFrame(sel_feature, columns=columns)


