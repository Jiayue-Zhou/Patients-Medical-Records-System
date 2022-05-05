from aggregation import encode


def transaction_upload(address, w3, contract, chain_id, private_key, instance):
    nonce = w3.eth.getTransactionCount(address)

    result = encode(instance)

    transaction = contract.functions.storeData(int(instance.covid19_Res), result) \
        .buildTransaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": nonce,
        }
    )
    signed_txn = w3.eth.account.sign_transaction(
        transaction, private_key=private_key
    )

    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    password = contract.functions.getPassword().call()
    return password

