from brownie import myFirstContract, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    my_First_Contract.deploy({'from': account})
    tx = my_First_Contract.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", my_First_Contract.getNumber({'from': account}))
 
def main():
    deployContract()
