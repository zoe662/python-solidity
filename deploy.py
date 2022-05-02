import sys

from solcx import compile_standard, install_solc
# install_solc('0.8.0')
from web3 import Web3
from config import *
import sys
import json

# compile and get abi&bytecode
def compile_sol(sol_file_location):
    # return bytecode, abi
    with open(sol_file_location,  "r") as f:
        sol = f.read()

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": sol}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.0"
    )


    bytecode = compiled_sol['contracts']['SimpleStorage.sol']['Storage']['evm']['bytecode']['object']

    abi = compiled_sol['contracts']['SimpleStorage.sol']['Storage']['abi']

    return abi, bytecode

def save_abi(abi):
    with open('abi.json', 'w') as f:
        f.write(json.dumps(abi))



def main():
    abi, bytecode = compile_sol("./SimpleStorage.sol")
    # print(abi)
    save_abi(abi)


    # connect
    w3 = Web3(Web3.HTTPProvider(HTTP))
    chain_id = CHAINID
    my_address = ADDRESS
    private_key = PRIVATEKEY

    # build
    SimpleStorate = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.getTransactionCount(my_address)
    transaction = SimpleStorate.constructor().buildTransaction(
        {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
    )

    # signed
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_addr = tx_receipt.contractAddress
    print(contract_addr)

if __name__ == "__main__":
    main()