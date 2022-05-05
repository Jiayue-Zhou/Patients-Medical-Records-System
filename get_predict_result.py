from initialize_my_contract import initialize
from model import algo
import pandas as pd

from process_data import pre_precess_for_model
from aggregation import decode

_, _, _, _, my_contract = initialize()


def take_all_data_from_blockchain():
    result = []
    pp = my_contract.functions.getTotal().call()
    for i in range(len(pp)):
        feats = decode(pp[i][2])
        covid_res = pp[i][1]
        feats.insert(1, covid_res)
        result.append(feats)
    dataset = pre_precess_for_model(result)
    print(f'We have {dataset.shape[0]} for current records number.')
    return dataset
    # algo(kk, dp)


def predict_for_datapoint(datapoint):
    print(f'Get the datapoint\n {datapoint}')
    print("Waiting...")
    all_data = take_all_data_from_blockchain()
    result = algo(all_data, datapoint)
    return result


# For test this function
if __name__ == '__main__':
    dp = pd.read_csv('C:/Users/zjy/Desktop/test_dataset.csv')
    predict_for_datapoint(dp)
