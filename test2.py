import json
from web3 import Web3
from solcx import compile_standard, install_solc

from transaction import transaction_upload
from process_data import processingData
from aggregation import decode, encode
from people import People

# from dotenv import load_dotenv

TEST_URL = "HTTP://127.0.0.1:7545"
MY_ADDRESS = "0xC69ae41CD528e21863CB96aA7F4a338DC808c314"
PRIVATE_KEY = "a356bc5e2ff4e1eaa40973460eeddefc56386ff4c742e5bd8e88da08ac1a1188"
CHAIN_ID = 1337
# load_dotenv()

CONTRACT_ADDRESS = "0x5E42C3942729A715FC1C564ee35B32bEfAf82627"

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


w3 = Web3(Web3.HTTPProvider(TEST_URL))

simple_storage = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

x = ""
while(x != "exit"):
    x = input()
    x = int(x)
    kk = simple_storage.functions.getData(x).call()
    kk = decode(kk)
    print(kk)
#hemoglobin
print("End of the program. Exit successfully.")