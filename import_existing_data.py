import json
from web3 import Web3
from solcx import compile_standard, install_solc
from transaction import transaction_upload
from process_data import processing_data
# from dotenv import load_dotenv

TEST_URL = "HTTP://127.0.0.1:8545"
MY_ADDRESS = "0xb7248a0173d8d7B1C9CF5735460ce42cE6f12FFC"
PRIVATE_KEY = "722f642aa9250770ceadea70d38ecb8a06a1d89d5fb184ee6e2f971ff27fb90b"
CHAIN_ID = 1337
# load_dotenv()

with open("./patientRecordContract.sol", "r") as file:
    smart_contract_file = file.read()

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"patientRecordContract.sol": {"content": smart_contract_file}},
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

w3 = Web3(Web3.HTTPProvider(TEST_URL))

MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.getTransactionCount(MY_ADDRESS)

transaction = MyContract.constructor().buildTransaction(
    {
        "chainId": CHAIN_ID,
        "gasPrice": w3.eth.gas_price,
        "from": MY_ADDRESS,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
print("Deploying Contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

with open("contractAddress", "w") as f:
    f.write(tx_receipt.contractAddress)

my_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

result = processing_data()

cnt = 1
for pp in result:
    print(f'People with {pp.age_quantile} has been uploaded.({cnt}/{len(result)})')
    transaction_upload(MY_ADDRESS, w3, my_contract, CHAIN_ID, PRIVATE_KEY, pp)
    cnt = cnt + 1
