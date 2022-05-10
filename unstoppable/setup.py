from deployContract import init_contract, get_addr, get_abi
from web3 import Web3
from config import *



w3 = Web3(Web3.HTTPProvider(HTTP))

addr = get_addr('DamnValuableToken')
abi = get_abi('DamnValuableToken')
DVT = w3.eth.contract(addr, abi=abi[0])

addr = get_addr('UnstoppableLendger')
abi = get_abi('UnstoppableLendger')
UnstoppableLendger = w3.eth.contract(addr, abi=abi[0])

addr = get_addr('RecieverUnstoppable')
abi = get_abi('RecieverUnstoppable')
RecieverUnstoppable = w3.eth.contract(addr, abi=abi[0])





def transfer100():
    nonce = w3.eth.getTransactionCount(OWNER_ADDR)
    transaction = DVT.functions.transfer(ATTACKER_ADDR, 100).buildTransaction(
        {"gasPrice": w3.eth.gas_price, "chainId": CHAINID, "from": OWNER_ADDR, "nonce": nonce}
    )

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=OWNER_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('transfer 100 DVT to attacker.')


def init():
    file_name = "DamnValuableToken"
    init_contract(file_name)
    DVTTocken = get_addr(file_name)

    # file_name = "UnstoppableLendger"
    # init_contract(file_name, struc={'poolAddress': DVTTocken})
    # ledgerPool = get_addr(file_name)

    file_name = "ReceiverUnstoppable"
    init_contract(file_name, struc={'poolAddress': DVTTocken})
    transfer100()

    print()
    print('INIT RESULT')
    print('DVT BALANCE:')
    balance = DVT.functions.balanceOf(OWNER_ADDR).call()
    print('OWNER: %s' % balance)

    balance = DVT.functions.balanceOf(ATTACKER_ADDR).call()
    print('ATTACKER: %s' % balance)


def main():
    init()
    print('ok')

if __name__ == "__main__":
    main()