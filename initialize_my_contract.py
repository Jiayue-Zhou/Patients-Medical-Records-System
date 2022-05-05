import json
from web3 import Web3
from solcx import compile_standard


def initialize():
    TEST_URL = "HTTP://127.0.0.1:8545"
    MY_ADDRESS = "0xb7248a0173d8d7B1C9CF5735460ce42cE6f12FFC"
    PRIVATE_KEY = "722f642aa9250770ceadea70d38ecb8a06a1d89d5fb184ee6e2f971ff27fb90b"
    CHAIN_ID = 1337
    # load_dotenv()

    with open("contractAddress", "r") as f:
        CONTRACT_ADDRESS = f.readline()

    print(f'Smart Contract Address is {CONTRACT_ADDRESS}')

    # CONTRACT_ADDRESS = "0x5E42C3942729A715FC1C564ee35B32bEfAf82627"

    with open("./patientRecordContract.sol", "r") as file:
        my_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"patientRecordContract.sol": {"content": my_file}},
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

    w3 = Web3(Web3.HTTPProvider(TEST_URL, request_kwargs={'timeout': 60}))

    my_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

    return MY_ADDRESS, CHAIN_ID, w3, PRIVATE_KEY, my_contract
