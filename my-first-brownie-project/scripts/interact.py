from brownie import myFirstContract, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"])
    my_First_Contract = myFirstContract[-1]
    tx = my_First_Contract.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", my_First_Contract.getNumber({'from': account}))
