import json
from web3 import Web3
from solcx import compile_standard, install_solc
from model import algo
import pandas as pd
from transaction import transaction_upload
from process_data import processingData, prePrecessForModel
from aggregation import decode, encode
from people import People

# from dotenv import load_dotenv

TEST_URL = "HTTP://127.0.0.1:7545"
MY_ADDRESS = "0xC69ae41CD528e21863CB96aA7F4a338DC808c314"
PRIVATE_KEY = "a356bc5e2ff4e1eaa40973460eeddefc56386ff4c742e5bd8e88da08ac1a1188"
CHAIN_ID = 1337
# load_dotenv()

with open("contractAddress", "r") as f:
    CONTRACT_ADDRESS = f.readline()

print(f'Smart Contract Address is {CONTRACT_ADDRESS}')

#CONTRACT_ADDRESS = "0x5E42C3942729A715FC1C564ee35B32bEfAf82627"

with open("./patientRecordContract.sol", "r") as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"patientRecordContract.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
)
abi = json.loads(
    compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["metadata"]
)["output"]["abi"]

# abi = json.loads(
#     compiled_code["contracts"]["patientRecordContract.sol"]["PatientRecord"]["metadata"]
# )["output"]["abi"]


w3 = Web3(Web3.HTTPProvider(TEST_URL, request_kwargs={'timeout': 60}))

simple_storage = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)


def takeAllDataFromBlockchain():
    # totalNumber = simple_storage.functions.getPeopleRecordNum().call()
    result = []
    # for i in range(totalNumber):
    #     print(f'Get data {i}')
    #     kk = simple_storage.functions.getData(i).call()
    #     kk = decode(kk)
    #     covidRes = simple_storage.functions.getCovidResult(x).call()
    #     kk.insert(1, covidRes)
    #     result.append(kk)
    #print("begin...")
    pp = simple_storage.functions.getTotal().call()
    #print(pp)
    for i in range(len(pp)):
        #print(i)
        kk = decode(pp[i][2])
        covidRes = pp[i][1]
        kk.insert(1, covidRes)
        result.append(kk)
    #print(result)
    kk = prePrecessForModel(result)
    dp = pd.read_csv('C:/Users/zjy/Desktop/test_dataset.csv')
    #print(dp)
    print(kk.shape)
    #print(kk)
    algo(kk, dp)

x = ""
while(x != "exit"):
    x = input()
    #x = int(x)
    print("Waiting...")
    allData = takeAllDataFromBlockchain()
    #kk = simple_storage.functions.getData(x).call()
    #covidRes = simple_storage.functions.getCovidResult(x).call()
    #kk = decode(kk)
    #kk.insert(1, covidRes)
    #prePrecessForModel(kk)
    #algo(kk)
    #print(kk)
#hemoglobin
print("End of the program. Exit successfully.")

