from brownie import myFirstContract, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    myFirstContract.deploy({'from': account})
 
def main():
    deployContract()
