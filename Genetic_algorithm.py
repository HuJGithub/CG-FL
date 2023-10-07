import numpy as np
import pandas as pd
import random
from data_process.ProcessedData import ProcessedData


class GA(ProcessedData):

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.rest_columns = raw_data.rest_columns


    def process(self):
        equal_zero_index = (self.label_df != 1).values
        equal_one_index = ~equal_zero_index

        pass_feature = np.array(self.feature_df[equal_zero_index])
        fail_feature = np.array(self.feature_df[equal_one_index])
        origin_df = np.array(self.feature_df)
        diff_num = len(pass_feature) - len(fail_feature)
        print(len(pass_feature),len(fail_feature))
        if diff_num < 1 or len(fail_feature) <= 0:
            return
        if len(fail_feature)==1:
            fail_feature=np.vstack((fail_feature,fail_feature))
        #temp_array = np.zeros([diff_num, len(self.feature_df.values[0])])
        for i in range(diff_num//2):
            temp1 = fail_feature[0]
            temp2 = fail_feature[1]
            for ft in fail_feature:
                if list(temp2).count(1) < list(temp1).count(1):
                    temp1,temp2 = temp2, temp1
                if list(temp2).count(1) > list(ft).count(1):
                    temp2 = ft
            j=np.random.randint(0, len(self.feature_df.values[0]))
            temp1[j],temp2[j]=temp2[j],temp1[j]
            fail_feature=np.vstack((fail_feature,temp1,temp2))


        compose_feature = np.vstack((pass_feature, fail_feature))
        #print(len(pass_feature),len(fail_feature))
        label_np = np.array(self.label_df)
        gen_label = np.ones(compose_feature.shape[0]-origin_df.shape[0]).reshape((-1, 1))
        compose_label = np.vstack((label_np, gen_label))

        self.label_df = pd.DataFrame(compose_label, columns=['error'], dtype=float)
        self.feature_df = pd.DataFrame(compose_feature, columns=self.feature_df.columns, dtype=float)

        self.data_df = pd.concat([self.feature_df, self.label_df], axis=1)
