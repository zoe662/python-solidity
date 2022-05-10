from setup import DVT, UnstoppableLendger, RecieverUnstoppable



balance = DVT_Contract.functions.balanceOf(OWNER_ADDR).call()
print(balance)

balance = DVT_Contract.functions.balanceOf(ATTACKER_ADDR).call()
print(balance)

