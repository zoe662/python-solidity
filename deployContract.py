import sys
from solcx import compile_standard
# install_solc('0.8.0')
from web3 import Web3
from config import *
import json


w3 = Web3(Web3.HTTPProvider(HTTP))

def compile_sol(file_name):
    sol_file_location = CONTRACTS_PATH + "./%s.sol" % file_name
    # return bytecode, abi
    with open(sol_file_location,  "r") as f:
        sol = f.read()

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {"%s.sol" % file_name: {"content": sol}},
        "settings": {
            "remappings": CONTRACT_REMAPPINGS,
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.0",
        allow_paths=[CONTRACTS_PATH],
        base_path=CONTRACTS_PATH
    )

    contracts = [c for c in compiled_sol['contracts'].keys() if not c.count('/')]
    for contract in contracts:
        contract = list(compiled_sol['contracts']['%s.sol' % file_name].keys())[0]
        bytecode = compiled_sol['contracts']['%s.sol' % file_name][contract]['evm']['bytecode']['object']

        abi = compiled_sol['contracts']['%s.sol' % file_name][contract]['abi']
        file_name = sol_file_location.split('/')[-1].split('.')[0]

        with open(CONTRACT_ABI_PATH + '%s.json' % contract, 'w') as f:
            f.write(json.dumps(abi, indent=4))

        with open(CONTRACT_ABI_PATH + '%s.txt' % contract, 'w') as f:
            f.write(bytecode)
        return abi, bytecode


def get_abi(file_name):
    with open(CONTRACT_ABI_PATH + '%s.json' % file_name, 'r') as f:
        abi = json.load(f)

    with open(CONTRACT_ABI_PATH + '%s.txt' % file_name, 'r') as f:
        bytecode = f.read()
    return list(abi), bytecode

def deploy_contract(file_name, struc={}):
    abi, bytecode = get_abi(file_name)
    w3 = Web3(Web3.HTTPProvider(HTTP))
    # build
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.getTransactionCount(OWNER_ADDR)
    constructors = {
        "gasPrice": w3.eth.gas_price, "chainId": CHAINID, "from": OWNER_ADDR, "nonce": nonce
    }
    if struc:
        transaction = contract.constructor(**struc).buildTransaction(constructors)
    else:
        transaction = contract.constructor().buildTransaction(constructors)
    # signed
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=OWNER_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_addr = tx_receipt.contractAddress

    with open(CONTRACTS_PATH+'%s.txt'%file_name, 'w') as f:
        f.write(contract_addr)

    print('deploy success!')

def init_contract(file_name, struc={}):
    compile_sol(file_name)
    deploy_contract(file_name, struc)

def get_addr(contract_name):
    with open(CONTRACTS_PATH + '%s.txt' % contract_name, 'r') as f:
        addr = f.read()
    return addr


def get_ontract(contract_name):
    addr = get_addr(contract_name)
    abi = get_abi(contract_name)
    return w3.eth.contract(addr, abi=abi[0])

def sign_ontract(msg_adr, msg_key, contract, constructors):
    nonce = w3.eth.getTransactionCount(msg_adr)
    transaction = contract.functions.transfer(**constructors).buildTransaction(
        {"gasPrice": w3.eth.gas_price, "chainId": CHAINID, "from": msg_adr, "nonce": nonce}
    )

    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=msg_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('signed contract: %s' % tx_hash)



def main():
    # build token
    file_name = "DamnValuableToken"
    init_contract(file_name)
    # build pool
    file_name = "ReceiverUnstoppable"
    dvt_pool = get_addr('DamnValuableToken')
    init_contract(file_name, struc={'poolAddress': dvt_pool})


if __name__ == "__main__":
    main()