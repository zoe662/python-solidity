import os
# GANACHE SETTINGS
HTTP = "HTTP://0.0.0.0:7545"
CHAINID = 1337

# GANACHE ACCOUNTS SETTINGS
OWNER_ADDR = "0x26B51C24270f1112768D6A5AEcF63D8993C42A9f"
OWNER_KEY = "d08ccbdf1897e6c5f775bf50320d68e4e0e31a2d883e85bdc9a114a7ea75d2b1"

ATTACKER_ADDR = "0x648e39c48BBC2C4c2147B2C00F45931D92Fe378A"
ATTACKER_KEY = "41faf262d28b5bfe16a3389355ad09bd720446b77a4baacaff9cc3b03e85efbe"

# PATH
# where all damn-vulnerable-defi contracts are
CONTRACTS_PATH = os.path.dirname(__file__) + '/contracts/'
# fix path problem in solidity
CONTRACT_REMAPPINGS = ['@openzeppelin=openzeppelin-contracts']
CONTRACT_ABI_PATH = os.path.dirname(__file__) + '/ABI/'
