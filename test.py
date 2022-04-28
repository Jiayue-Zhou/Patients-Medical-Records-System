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

with open("./patientRecordContract.sol", "r") as file:
    simple_storage_file = file.read()

install_solc("0.8.0")

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

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["evm"][
    "bytecode"
]["object"]

abi = json.loads(
    compiled_sol["contracts"]["patientRecordContract.sol"]["PatientRecord"]["metadata"]
)["output"]["abi"]

# print(bytecode)
# print(compiled_sol)

w3 = Web3(Web3.HTTPProvider(TEST_URL))

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# print(SimpleStorage)
nonce = w3.eth.getTransactionCount(MY_ADDRESS)

transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": CHAIN_ID,
        "gasPrice": w3.eth.gas_price,
        "from": MY_ADDRESS,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
print("Deploying Contract!")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
#print(type(tx_receipt.contractAddress))

with open("contractAddress", "w") as f:
    f.write(tx_receipt.contractAddress)

simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# def transaction(address, w3, contract, chain_id, private_key)

# p1 = People(17, 0, "0.056260044")
# p2 = People(1, 0, "-0.664133646")

result = processingData()

cnt = 1
for pp in result:
    print(f'People with {pp.age_quantile} has been uploaded.({cnt}/{len(result)})')
    transaction_upload(MY_ADDRESS, w3, simple_storage, CHAIN_ID, PRIVATE_KEY, pp)
    cnt = cnt + 1

# 0 1
# x = ""
# while(x != "exit"):
#     x = input()
#     x = int(x)
#     kk = simple_storage.functions.getData(x).call()
#     kk = decode(kk)
#     print(kk)
# #hemoglobin
# print("End of the program. Exit successfully.")
# print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")

# print(nonce)
