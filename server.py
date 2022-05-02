from web3 import Web3
from config import *
import json

def load_abi():
    with open('abi.json', 'r') as f:
        # print(f.read())
        abi = json.load(f)
    return abi


w3 = Web3(Web3.HTTPProvider(HTTP))
chain_id = CHAINID
my_address = ADDRESS
private_key = PRIVATEKEY
abi = load_abi()

contract_addr = '0x1b368C946BE7A773BEA11238Ba0D87C11dbf1642'

contract = w3.eth.contract(address=contract_addr, abi=abi)

store = contract.functions.store(1).call()
print(store)
retrieve = contract.functions.retrieve().call()
print(retrieve)

nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
transaction = contract.functions.store(1).buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
)

signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

retrieve = contract.functions.retrieve().call()
print(retrieve)