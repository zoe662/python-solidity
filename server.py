from web3 import Web3
from config import *
from deployContract import get_addr, get_abi


w3 = Web3(Web3.HTTPProvider(HTTP))
addr = get_addr('DamnValuableToken')
abi = get_abi('DamnValuableToken')
contract = w3.eth.contract(addr, abi=abi[0])

balance = contract.functions.balanceOf(OWNER_ADDR).call()
print(balance)

# balance = contract.functions.totalSupply().call()
# print(balance)
# store = contract.functions.store(1).call()
# print(store)
# retrieve = contract.functions.retrieve().call()
# print(retrieve)
#
# nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)
# transaction = contract.functions.store(1).buildTransaction(
#     {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
# )
#
# signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#
# retrieve = contract.functions.retrieve().call()
# print(retrieve)