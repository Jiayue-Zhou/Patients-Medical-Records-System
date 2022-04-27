from aggregation import encode

def transaction_upload(address, w3, contract, chain_id, private_key, instance):

    nonce = w3.eth.getTransactionCount(address)
    #print("nonce:", nonce)
    result = encode(instance)
    #print("Transaction uploading...")
    greeting_transaction = contract.functions.storeData(int(instance.covid19_Res), result)\
        .buildTransaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": nonce,
        }
    )
    #print("Transaction signing...")
    signed_greeting_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key
    )
    #print("Finished!")
    tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
